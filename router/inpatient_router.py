from fastapi import APIRouter, HTTPException
from model.inpatient_dto import InpatientDTO
from services.inpatient_service import InpatientService

inpatient_router = APIRouter()
inpatient_service = InpatientService()

@inpatient_router.post("/inpatients/")
def add_inpatient(inpatient: InpatientDTO):
    return inpatient_service.add_inpatient(inpatient)

@inpatient_router.get("/inpatients/{patient_id}")
def get_inpatient(patient_id: int):
    inpatient = inpatient_service.get_inpatient(patient_id)
    if not inpatient:
        raise HTTPException(status_code=404, detail="Inpatient not found")
    return inpatient
