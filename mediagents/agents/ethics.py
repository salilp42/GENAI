"""
Ethics agent implementation.
"""

import asyncio
import random
from typing import List, Tuple

class EthicsAgent:
    """
    Ensures compliance with medical ethics guidelines asynchronously.
    """
    def __init__(self):
        self.name = "Ethics"

    async def arun(self, recommendations: List[Tuple[str, float, str]]):
        checks = []
        for (diag, score, info) in recommendations:
            checks.append(asyncio.create_task(self.check_ethics(diag, score, info)))
        results = await asyncio.gather(*checks)
        return results

    async def check_ethics(self, diag: str, score: float, info: str):
        await asyncio.sleep(0.05)  # simulate some I/O
        # If confidence is very low, we might veto
        veto = (score < 0.3 and random.random() > 0.5)
        return diag, score, info, veto
