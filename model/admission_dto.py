from pydantic import BaseModel

class AdmissionDTO(BaseModel):
    patient_name: str
    patient_surname: str
    age: int
    gender: str
    contact: str
    address: str
    admitted_on: str
    reason: str
