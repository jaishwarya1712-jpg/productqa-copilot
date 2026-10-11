evaluation_cases = [
    {
        "name": "Simple UI Copy Change",
        "requirement": 'Change the homepage heading from "Welcome" to "Welcome Back".',
        "expected_readiness": "READY",
    },
    {
        "name": "Ambiguous Payment Requirement",
        "requirement": "Users should be able to purchase a gift card using UPI.",
        "expected_readiness": "NEEDS CLARIFICATION",
    },
    {
        "name": "Very Vague Requirement",
        "requirement": "Improve the checkout experience.",
        "expected_readiness": "NOT READY",
    },
    {
    "name": "Explicit Failure Handling",
    "requirement": (
        "If a UPI payment fails, show an error message "
        "and allow the user to retry the payment."
    ),
    "expected_readiness": "READY",
},
{
    "name": "Explicit Transaction Limit",
    "requirement": (
        "Users can transfer up to ₹10,000 per transaction. "
        "If the amount exceeds ₹10,000, prevent the transfer "
        "and display an error message."
    ),
    "expected_readiness": "READY",
},
{
    "name": "Conflicting Requirement",
    "requirement": (
        "Users must be logged in to purchase a gift card. "
        "Guest users should also be able to purchase a gift card "
        "without logging in."
    ),
    "expected_readiness": "NOT READY",
},
{
    "name": "Integration Keyword False Positive",
    "requirement": (
        "Users can integrate ideas from previous drafts "
        "into the final description."
    ),
    "expected_readiness": "NEEDS CLARIFICATION",
},
{
    "name": "Detailed Payment Requirement",
    "requirement": (
        "Authenticated users should be able to purchase a gift card "
        "using UPI. If the payment succeeds, confirm the purchase. "
        "If the payment fails, show an error and allow the user to retry."
    ),
    "expected_readiness": "READY",

},
{
    "name": "Return Visit Conditional Heading",
    "requirement": (
        'Change the homepage heading from "Welcome" to "Welcome Back" '
        'every time the user comes back to the app after visiting it '
        'once on the same day, based on server time zone.'
    ),
    "expected_readiness": "NEEDS CLARIFICATION",
},
]
from agent import analyze_requirement

passed = 0
failed = 0
errors = 0

for case in evaluation_cases:

    print("\n------------------------------")
    print("Test:", case["name"])

    analysis = analyze_requirement(case["requirement"])

    if analysis:
        actual_readiness = analysis.readiness.classification
        expected_readiness = case["expected_readiness"]

        #print("Expected:", expected_readiness)
        #print("Actual:", actual_readiness)
        print("Expected:", expected_readiness)
        print("Actual:", actual_readiness)
        print("Reasoning:", analysis.readiness.reasoning)
        print(
            "Blocking Clarifications:",
            analysis.readiness.blocking_clarifications
)

    if actual_readiness == expected_readiness:
       print("Result: PASS")
       passed += 1
    else:
        print("Result: FAIL")
        failed += 1

    else:
        print("Result: ERROR")
        errors += 1

 total = len(evaluation_cases)

print("\n==============================")
print("EVALUATION SUMMARY")
print("==============================")

print("Total Cases:", total)
print("Passed:", passed)
print("Failed:", failed)
print("Errors:", errors)       