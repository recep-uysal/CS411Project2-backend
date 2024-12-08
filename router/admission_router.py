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

@admission_router.get("/admissions/{admission_id}")
def get_admission(admission_id):
    admission = admission_service.get_admission(admission_id)
    if admission:
        return admission
    raise HTTPException(status_code=404, detail="Admission not found")

@admission_router.put("/admissions/{admission_id}")
def update_admission(admission_id, admission: AdmissionDTO):
    admission_service.update_admission(admission_id, admission)
    return {"message": "Admission updated successfully"}


# delete an admission record
@admission_router.delete("/admissions/{admission_id}")
def delete_admission(admission_id):
    admission = admission_service.get_admission(admission_id)
    if admission:
        admission_service.delete_admission(admission_id)
        return {"message": "Admission deleted successfully"}
    raise HTTPException(status_code=404, detail="Admission not found")

# get all admissions for a patient
@admission_router.get("/patients/{patient_id}/admissions/")
def get_patient_admissions(patient_id):
    return admission_service.get_patient_admissions(patient_id)
