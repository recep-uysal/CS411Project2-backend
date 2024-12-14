from fastapi import APIRouter, HTTPException
from services.user_management_service import UserManagementService

user_management_router = APIRouter()
user_management_service = UserManagementService()


#get all inpatients
@user_management_router.get("/get_all")
def get_all_inpatients():
    return user_management_service.get_all_users()

"""
# route to update inpatient
@user_management_router.put("/inpatients/{inpatient_id}")
def update_inpatient( inpatient_id: str, inpatient: InpatientDTO):
    return user_management_service.update_inpatient(inpatient_id,inpatient)

# route to delete inpatient
@user_management_router.delete("/inpatients/{inpatient_id}")
def delete_inpatient(inpatient_id):
    return user_management_service.delete_inpatient(inpatient_id)
"""
