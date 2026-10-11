import streamlit as st

from agent import analyze_requirement


st.set_page_config(
    page_title="ProductQA Copilot",
    page_icon="🔍",
    layout="wide",
)


st.title("ProductQA Copilot")

st.caption(
    "Review requirements for clarity, readiness, product risks, "
    "and QA coverage before implementation."
)


requirement = st.text_area(
    "Enter a product requirement",
    placeholder='Example: Change the homepage heading from "Welcome" to "Welcome Back".',
    height=150,
)


analyze_button = st.button(
    "Analyze Requirement",
    type="primary",
)


if analyze_button:

    if not requirement.strip():
        st.warning("Please enter a product requirement before analyzing.")

    else:
        with st.spinner("Analyzing requirement..."):
            analysis = analyze_requirement(requirement)

        if analysis:
            st.success("Analysis complete!")

            # ---------------------------------
            # Requirement Readiness
            # ---------------------------------

            st.subheader("Requirement Readiness")

            st.metric(
                label="Status",
                value=analysis.readiness.classification,
            )

            st.write(analysis.readiness.reasoning)

            st.markdown("**Blocking Clarifications**")

            blocking_clarifications = [
                clarification
                for clarification in analysis.readiness.blocking_clarifications
                if clarification.strip().lower() != "none"
            ]  

            if blocking_clarifications:
                for clarification in blocking_clarifications:
                    st.markdown(f"- {clarification}")
            else:
                st.write("None")

            # ---------------------------------
            # Requirement Summary
            # ---------------------------------

            st.subheader("Requirement Summary")
            st.write(analysis.requirement_summary)


            # ---------------------------------
            # Product and QA Tabs
            # ---------------------------------

            product_tab, qa_tab = st.tabs(
                ["Product Analysis", "QA Analysis"]
            )


            # PRODUCT TAB

            with product_tab:

                st.markdown("### Gaps & Ambiguities")

                if analysis.requirement_gaps:
                    for gap in analysis.requirement_gaps:
                        st.markdown(f"- {gap}")
                else:
                    st.write("None identified.")


                st.markdown("### Clarifying Questions")

                if analysis.clarifying_questions:
                    for question in analysis.clarifying_questions:
                        st.markdown(f"- {question}")
                else:
                    st.write("None identified.")


                st.markdown("### User Journeys & States")

                if analysis.user_journeys:
                    for journey in analysis.user_journeys:
                        st.markdown(f"- {journey}")
                else:
                    st.write("None identified.")


                st.markdown("### Acceptance Criteria Assessment")

                st.write(
                    analysis.acceptance_criteria_assessment
                )


                st.markdown("### Product / UX / Quality Risks")

                if analysis.risks:
                    for risk in analysis.risks:
                        st.markdown(f"- {risk}")
                else:
                    st.write("None identified.")


            # QA TAB

            with qa_tab:

                st.markdown("### QA Scenarios")


                st.markdown("**Positive**")

                if analysis.qa_scenarios.positive:
                    for scenario in analysis.qa_scenarios.positive:
                        st.markdown(f"- {scenario}")
                else:
                    st.write("None identified.")


                st.markdown("**Negative**")

                if analysis.qa_scenarios.negative:
                    for scenario in analysis.qa_scenarios.negative:
                        st.markdown(f"- {scenario}")
                else:
                    st.write("None identified.")


                st.markdown("**Boundary**")

                if analysis.qa_scenarios.boundary:
                    for scenario in analysis.qa_scenarios.boundary:
                        st.markdown(f"- {scenario}")
                else:
                    st.write("None identified.")


                st.markdown("**Edge Cases**")

                if analysis.qa_scenarios.edge_cases:
                    for scenario in analysis.qa_scenarios.edge_cases:
                        st.markdown(f"- {scenario}")
                else:
                    st.write("None identified.")


                st.markdown("### Technical Considerations")

                if analysis.technical_considerations:
                    for consideration in analysis.technical_considerations:
                        st.markdown(f"- {consideration}")
                else:
                    st.write("None identified.")


            # ---------------------------------
            # Assumptions
            # ---------------------------------

            st.subheader("Assumptions")

            if analysis.assumptions:
                for assumption in analysis.assumptions:
                    st.markdown(f"- {assumption}")
            else:
                st.write("No assumptions required.")


        else:
            st.error(
                "ProductQA could not complete the analysis. "
                "Please try again."
            )