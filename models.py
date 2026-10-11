from typing import Literal
from pydantic import BaseModel

class ReadinessAssessment(BaseModel):
    classification: Literal[
    "READY",
    "NEEDS CLARIFICATION",
    "NOT READY"
]
    reasoning: str
    blocking_clarifications: list[str]


class QAScenarios(BaseModel):
    positive: list[str]
    negative: list[str]
    boundary: list[str]
    edge_cases: list[str]

class ProductQAAnalysis(BaseModel):
    requirement_summary: str
    requirement_gaps: list[str]
    clarifying_questions: list[str]
    user_journeys: list[str]
    acceptance_criteria_assessment: str
    qa_scenarios: QAScenarios
    technical_considerations: list[str]
    risks: list[str]
    assumptions: list[str]
    readiness: ReadinessAssessment