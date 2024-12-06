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


# route to update inpatient
@inpatient_router.put("/inpatients/{patient_id}")
def update_inpatient(patient_id: int, inpatient: InpatientDTO):
    return inpatient_service.update_inpatient(patient_id, inpatient)

# route to delete inpatient
@inpatient_router.delete("/inpatients/{patient_id}")
def delete_inpatient(patient_id: int):
    return inpatient_service.delete_inpatient(patient_id)


#get all inpatients
@inpatient_router.get("/inpatients/")
def get_all_inpatients():
    return inpatient_service.get_all_inpatients()

# get all inpatients of a user
@inpatient_router.get("/inpatients/user/{user_id}")
def get_all_inpatients_by_user(user_id: int):
    return inpatient_service.get_all_inpatients_by_user(user_id)

# get all inpatients of a department
@inpatient_router.get("/inpatients/department/{department_id}")
def get_all_inpatients_by_department(department_id: int):
    return inpatient_service.get_all_inpatients_by_department(department_id)

# delete all inpatients
@inpatient_router.delete("/inpatients/")
def delete_all_inpatients():
    return inpatient_service.delete_all_inpatients()
