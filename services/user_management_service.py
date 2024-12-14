from crud.admin_crud import AdminCRUD
from model.user_dto import UserDtoForAdmin

class UserManagementService:
    def __init__(self):
        self.user_management_crud = AdminCRUD()

    def get_all_users(self):
        return self.user_management_crud.get_all_users()

    def update_user(self, user_id: str, user: UserDtoForAdmin):
        return self.user_management_crud.update_inpatient(user_id, user)

    def delete_user(self, user_id, user_email):
        return self.user_management_crud.delete_user(user_id, user_email)
    