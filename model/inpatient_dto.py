from pydantic import BaseModel
from typing import Optional


class InpatientDTO(BaseModel):
    patient_admission_id: str
    department_id: int
    room_number: int
    entrance_date: str
    discharge_date: Optional[str] = None
    status: str

class InpatientAddDTO(BaseModel):
    government_id : str
    room_number: int
    
    
    
class updateDTO(BaseModel):
    department_id: int
    room_number: int
    status: str
