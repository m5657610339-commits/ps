def home_fallback(data):
    budget = data["budget"]
    return {
        "category": "Home",
        "budget": budget,
        "summary": f"Suggested allocation for a {data['style']} {data['room']} setup.",
        "items": [
            {"name": "LED Ceiling Light", "estimated_price": round(budget * .12, 2), "platform": "Amazon"},
            {"name": "Decorative Wall Art", "estimated_price": round(budget * .15, 2), "platform": "IKEA"},
            {"name": "Storage / Side Table", "estimated_price": round(budget * .28, 2), "platform": "Flipkart"},
            {"name": "Curtains / Soft Furnishing", "estimated_price": round(budget * .20, 2), "platform": "Amazon"},
            {"name": "Decor Accessories", "estimated_price": round(budget * .15, 2), "platform": "IKEA"}
        ]
    }

def party_fallback(data):
    budget = data["budget"]
    return {
        "category": "Party",
        "budget": budget,
        "guests": data["guests"],
        "allocation": {
            "food": round(budget * .45, 2),
            "decoration": round(budget * .20, 2),
            "venue": round(budget * .25, 2),
            "entertainment": round(budget * .10, 2)
        },
        "suggestions": [
            "Compare catering packages for the guest count.",
            "Use simple themed decorations to control costs.",
            "Reserve part of the budget for unexpected expenses."
        ]
    }

def jewelry_fallback(data):
    budget = data["budget"]
    return {
        "category": "Jewelry",
        "budget": budget,
        "occasion": data["occasion"],
        "style": data["style"],
        "suggestions": [
            {"name": "Minimal Necklace Set", "estimated_price": round(budget * .35, 2), "platform": "Amazon"},
            {"name": "Matching Earrings", "estimated_price": round(budget * .25, 2), "platform": "Flipkart"},
            {"name": "Bracelet / Bangles", "estimated_price": round(budget * .20, 2), "platform": "Amazon"}
        ],
        "note": "For image-based matching, provide the outfit image and use the Gemini integration."
    }
