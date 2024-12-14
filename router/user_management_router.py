from fastapi import APIRouter, HTTPException
from services.user_management_service import UserManagementService
from model.user_dto import UserDtoForAdmin

user_management_router = APIRouter()
user_management_service = UserManagementService()


#get all inpatients
@user_management_router.get("/get_all")
def get_all_inpatients():
    return user_management_service.get_all_users()

@user_management_router.put("/update/{id}")
def update_inpatient( id, user: UserDtoForAdmin):
    return user_management_service.update_user(id, user)

@user_management_router.delete("/delete/{id}/{email}")
def delete_user(id, email):
    return user_management_service.delete_user(id, email)



