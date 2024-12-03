from pydantic import BaseModel

class AdmissionDTO(BaseModel):
    name: str
    surname: str
    age: int
    gender: str
    contact: str
    address: str
    admitted_on: str
    reason: str
