from pydantic import BaseModel
from typing import Optional

class InpatientDTO(BaseModel):
    patient_id: int
    department: str
    room_number: str
    admission_date: str
    discharge_date: Optional[str] = None
    status: str
    
    
