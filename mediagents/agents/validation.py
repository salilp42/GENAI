"""
Validation agent implementation.
"""

import asyncio
import random
from typing import List, Tuple
from ..knowledge.graph import MedicalKnowledgeGraph

class ValidationAgent:
    """
    Checks knowledge graph + UMLS consistency asynchronously.
    """
    def __init__(self, knowledge_graph: MedicalKnowledgeGraph):
        self.name = "Validation"
        self.kg = knowledge_graph

    async def arun(self, recommendations: List[Tuple[str, float, str, bool]]):
        tasks = []
        for (diag, score, info, veto) in recommendations:
            tasks.append(asyncio.create_task(self.validate_one(diag, score, info, veto)))
        results = await asyncio.gather(*tasks)
        return results

    async def validate_one(self, diag: str, score: float, info: str, veto: bool):
        await asyncio.sleep(0.02)  # simulate I/O
        if veto:
            return diag, score, info, veto, False

        kg_consistent = self.kg.is_consistent(diag)
        umls_consistent = random.random() > 0.1  # mock UMLS check

        return diag, score, info, veto, (kg_consistent and umls_consistent)
