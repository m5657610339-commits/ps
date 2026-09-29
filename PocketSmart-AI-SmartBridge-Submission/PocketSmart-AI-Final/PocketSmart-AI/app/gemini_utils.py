import os, json

def generate_with_gemini(prompt: str, image_bytes: bytes | None = None):
    """
    Optional Gemini integration.
    Set GEMINI_API_KEY and install google-genai to enable it.
    The application falls back to deterministic recommendations when unavailable.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return None
    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        contents = [prompt]
        if image_bytes:
            contents.append(image_bytes)
        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
            contents=contents
        )
        return response.text
    except Exception:
        return None

def build_prompt(category: str, data: dict):
    return (
        f"You are PocketSmart AI, a budget recommendation assistant. "
        f"Return concise JSON only. Category: {category}. "
        f"User data: {json.dumps(data)}. "
        f"Keep total recommendations within the stated budget and clearly label estimated prices."
    )
