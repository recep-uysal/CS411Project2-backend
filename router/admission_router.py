from fastapi import APIRouter, HTTPException
from model.admission_dto import AdmissionDTO
from services.admission_service import AdmissionService

admission_router = APIRouter()
admission_service = AdmissionService()

@admission_router.post("/admissions/")
def admit_patient(admission: AdmissionDTO):
    return admission_service.admit_patient(admission)

@admission_router.get("/admissions/")
def list_admissions():
    return admission_service.list_admissions()
