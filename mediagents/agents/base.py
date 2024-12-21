"""
Base agent implementations and mixins.
"""

import random
from typing import List
try:
    import numpy as np
except ImportError:
    np = None

class ThompsonSamplingMixin:
    """
    Mixin to demonstrate a simple approach to Thompson sampling for decision confidence.
    """
    def calculate_confidence(self, success_history: List[bool]) -> float:
        """
        success_history: a list of booleans indicating past successes/failures.
        Return a sample from Beta distribution as a confidence measure.
        """
        if not success_history or np is None:
            # If no history or numpy missing, fallback to random
            return random.uniform(0.5, 0.9)
        alpha = 1 + sum(success_history)
        beta = 1 + (len(success_history) - sum(success_history))
        return float(np.random.beta(alpha, beta))
