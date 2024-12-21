"""
Agent implementations for the MediAgents framework.
"""

import time
import logging
from typing import Dict, Any, Tuple, List

from ..models.data_models import PatientCase, AppValidationError
from ..knowledge.graph import MedicalKnowledgeGraph
from ..utils.metrics import MetricsCollector
from .diagnostician import DiagnosticianAgent
from .research import ResearchAgent
from .ethics import EthicsAgent
from .validation import ValidationAgent
from .explainability import ExplainabilityAgent

class ChiefMedicalOfficerAgent:
    """
    Central orchestrator that uses async to parallelize agent steps.
    """
    def __init__(self, knowledge_graph: MedicalKnowledgeGraph):
        self.diagnostician = DiagnosticianAgent(success_history=[True, False, True])
        self.research = ResearchAgent()
        self.ethics = EthicsAgent()
        self.validation = ValidationAgent(knowledge_graph)
        self.explain = ExplainabilityAgent()

    async def run_pipeline(self, patient_data: Dict[str, Any]):
        """
        Orchestrate the entire agent flow asynchronously.
        """
        try:
            patient_case = PatientCase(**patient_data)
        except ValidationError as ve:
            raise AppValidationError(f"Patient data invalid: {ve}")

        # Run the pipeline
        diag_results = await self.diagnostician.arun(patient_case)
        research_results = await self.research.arun(diag_results)
        ethics_results = await self.ethics.arun(research_results)
        validated = await self.validation.arun(ethics_results)
        explanations = self.explain.run(validated)

        # Build final decisions
        final_decisions = []
        for (diag, score, info, veto, valid), explanation in zip(validated, explanations):
            if (not veto) and valid:
                final_decisions.append({
                    "diagnosis": diag,
                    "confidence": score,
                    "explanation": explanation
                })

        return final_decisions, explanations
