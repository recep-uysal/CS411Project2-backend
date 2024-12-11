from fastapi import APIRouter, HTTPException
from model.inpatient_dto import InpatientDTO, InpatientAddDTO
from model.inpatient_dto import updateDTO
from services.inpatient_service import InpatientService

inpatient_router = APIRouter()
inpatient_service = InpatientService()

@inpatient_router.post("/inpatients/")
def add_inpatient(inpatient: InpatientAddDTO):
    return inpatient_service.add_inpatient(inpatient)

@inpatient_router.get("/inpatients/{inpatient_id}")
def get_inpatient(inpatient_id):
    inpatient = inpatient_service.get_inpatient(inpatient_id)
    if not inpatient:
        raise HTTPException(status_code=404, detail="Inpatient not found")
    return inpatient


# route to update inpatient
@inpatient_router.put("/inpatients/{inpatient_id}")
def update_inpatient( inpatient_id: str, inpatient: InpatientDTO):
    return inpatient_service.update_inpatient(inpatient_id,inpatient)

# route to delete inpatient
@inpatient_router.delete("/inpatients/{inpatient_id}")
def delete_inpatient(inpatient_id):
    return inpatient_service.delete_inpatient(inpatient_id)


#get all inpatients
@inpatient_router.get("/inpatients/")
def get_all_inpatients():
    return inpatient_service.get_all_inpatients()

# get all inpatients of a user
@inpatient_router.get("/inpatients/user/{government_id}")
def get_all_inpatients_by_government_id(government_id: int):
    return inpatient_service.get_all_inpatients_by_government_id(government_id)

# get all inpatients of a department
@inpatient_router.get("/inpatients/department/{department_id}")
def get_all_inpatients_by_department(department_id: int):
    return inpatient_service.get_all_inpatients_by_department(department_id)

# delete all inpatients
@inpatient_router.delete("/inpatients/")
def delete_all_inpatients():
    return inpatient_service.delete_all_inpatients()

# discharge inpatient
@inpatient_router.put("/inpatients/discharge/{inpatient_id}")
def discharge_inpatient(inpatient_id):
    return inpatient_service.discharge_inpatient(inpatient_id)

# update department and room of inpatient
@inpatient_router.put("/inpatients/update_department_room_status/{inpatient_id}")
def update_department_room_status(inpatient_id: str, update: updateDTO):
    return inpatient_service.update_department_room_status(inpatient_id, update)
