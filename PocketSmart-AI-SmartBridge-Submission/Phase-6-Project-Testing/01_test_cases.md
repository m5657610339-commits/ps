# Phase 6 – Project Testing

## Test Cases

| ID | Test | Expected Result |
|---|---|---|
| TC01 | Health endpoint | Returns healthy status |
| TC02 | Register new user | User is created |
| TC03 | Register duplicate email | Request is rejected |
| TC04 | Login valid credentials | JWT token returned |
| TC05 | Login invalid credentials | Authentication rejected |
| TC06 | Home planner with valid budget | Recommendation returned |
| TC07 | Party planner with valid guest count | Party allocation returned |
| TC08 | Jewelry planner without image | Text-based recommendation returned |
| TC09 | Jewelry planner with image | Image is accepted for optional AI analysis |
| TC10 | History request | Previous recommendations returned |
| TC11 | Missing authentication | Protected route rejects request |
| TC12 | Invalid/negative budget | Validation rejects input |

## Optimization
Testing should include different budgets, preferences and real-world scenarios. The project document specifically calls for evaluating response quality, budget adherence, platform accuracy, prompts, validations and fallback behavior.
