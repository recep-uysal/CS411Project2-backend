from pydantic import BaseModel

class AdmissionDTO(BaseModel):
    government_id: int
    patient_name: str
    patient_surname: str
    age: int
    gender: str
    contact: str
    address: str
    admitted_on: str
    insurance: str
    department_id: int

class UpdateAdmissionDTO(BaseModel):
    patient_name: str
    patient_surname: str
    age: int
    gender: str
    contact: str
    address: str
    insurance: str
    department_id: int
