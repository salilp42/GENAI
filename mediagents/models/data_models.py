"""
Data models and error handling for the MediAgents framework.
"""

from typing import List, Optional
from pydantic import BaseModel

class AgentError(Exception):
    """Custom error for Agent failures."""
    pass

class AppValidationError(AgentError):
    """Raised when data fails validation."""
    pass

class PatientCase(BaseModel):
    """Pydantic data model for patient case."""
    patient_id: str
    symptoms: List[str]
    age: int
    medical_history: Optional[List[str]] = []
