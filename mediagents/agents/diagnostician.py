"""
Diagnostician agent implementation.
"""

from typing import List, Tuple
from langchain.agents import Tool, AgentExecutor
from langchain.llms import OpenAI
from langchain.agents.agent import BaseMultiActionAgent

from ..models.data_models import PatientCase
from .base import ThompsonSamplingMixin

class DiagnosticianAgent(BaseMultiActionAgent, ThompsonSamplingMixin):
    """
    Analyzes symptoms (async).
    Demonstrates partial LangChain integration with Tools + a Thompson sampling approach.
    """

    def __init__(self, success_history=None):
        super().__init__()
        self.name = "Diagnostician"
        self.success_history = success_history if success_history else []
        self.llm = OpenAI(temperature=0)
        self.tools = [
            Tool(name="analyze_symptoms", func=self.analyze_symptoms),
        ]

    async def arun(self, patient_case: PatientCase) -> List[Tuple[str, float]]:
        """
        Asynchronously run the agent's logic to propose diagnoses.
        """
        base_conf = self.calculate_confidence(self.success_history)
        diagnoses = []
        if "fever" in patient_case.symptoms:
            diagnoses.append(("Infection", base_conf))
        if "cough" in patient_case.symptoms:
            diagnoses.append(("Respiratory condition", base_conf * 0.9))
        if patient_case.age > 60:
            diagnoses.append(("Age-related vulnerability", base_conf * 0.8))
        return diagnoses

    def analyze_symptoms(self, input_data: str) -> str:
        return "Analyzed symptoms result."
