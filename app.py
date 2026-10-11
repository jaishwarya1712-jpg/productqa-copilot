from agent import analyze_requirement


print("Welcome to ProductQA Copilot!")

requirement = input("\nEnter a product requirement: ")

if requirement:
    print("\nAnalyzing requirement...\n")

    analysis = analyze_requirement(requirement)

    if analysis:
        print("\nProductQA Analysis:\n")

        print("1. Requirement Summary")
        print(analysis.requirement_summary)

        print("\n2. Requirement Gaps & Ambiguities")
        for gap in analysis.requirement_gaps:
            print("-", gap)

        print("\n3. Clarifying Questions")
        for question in analysis.clarifying_questions:
            print("-", question)

        print("\n4. User Journeys & States")
        for journey in analysis.user_journeys:
            print("-", journey)

        print("\n5. Acceptance Criteria Assessment")
        print(analysis.acceptance_criteria_assessment)

        print("\n6. QA Scenarios")

        print("Positive:")
        for scenario in analysis.qa_scenarios.positive:
            print("-", scenario)

        print("Negative:")
        for scenario in analysis.qa_scenarios.negative:
            print("-", scenario)

        print("Boundary:")
        for scenario in analysis.qa_scenarios.boundary:
            print("-", scenario)

        print("Edge Cases:")
        for scenario in analysis.qa_scenarios.edge_cases:
            print("-", scenario)

        print("\n7. Technical Considerations")
        for consideration in analysis.technical_considerations:
            print("-", consideration)

        print("\n8. Product / UX / Quality Risks")
        for risk in analysis.risks:
            print("-", risk)

        print("\n9. Assumptions")
        for assumption in analysis.assumptions:
            print("-", assumption)

        print("\n10. Readiness Assessment")
        print("Classification:", analysis.readiness.classification)
        print("Reasoning:", analysis.readiness.reasoning)

        print("Blocking Clarifications:")

if analysis.readiness.blocking_clarifications:
    for clarification in analysis.readiness.blocking_clarifications:
        print("-", clarification)
else:
    print("None")

    else:
        print("\nProductQA could not complete the analysis. Please try again.")

else:
    print("\nPlease enter a requirement.")