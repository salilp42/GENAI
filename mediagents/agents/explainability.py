"""
Explainability agent implementation.
"""

from typing import List, Tuple

class ExplainabilityAgent:
    """
    Generates human-readable rationales for the final decisions.
    """
    def __init__(self):
        self.name = "Explainability"

    def run(self, validated_recommendations: List[Tuple[str, float, str, bool, bool]]) -> List[str]:
        explanations = []
        for (diag, score, info, veto, valid) in validated_recommendations:
            if veto:
                rationale = f"Diagnosis '{diag}' was vetoed by Ethics Agent due to risk."
            elif not valid:
                rationale = f"Diagnosis '{diag}' failed validation checks."
            else:
                rationale = (
                    f"Diagnosis '{diag}' accepted with confidence {score:.2f}. "
                    f"PubMed / Research note: {info}"
                )
            explanations.append(rationale)
        return explanations
