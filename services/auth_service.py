# services/auth_service.py
from config.encryption import Encrypter
from crud.user_crud import UserCRUD
from model.user_dto import new_user_dto

class AuthService:
    def __init__(self):
        self.user_crud = UserCRUD()
        self.encrypter = Encrypter()

    def verify_user_credentials(self, email: str, password: str):
        user = self.user_crud.get_user_by_email_and_password(email, password)
        if not user:
            return None

        return user

    def register_user(self, new_user: new_user_dto):
        existing_user = self.user_crud.get_user_by_email(new_user.email)
        if existing_user:
            raise ValueError("Email is already registered")

        self.user_crud.add_user(new_user)

    def authenticate_user(self, email: str, password: str):
        user = self.user_crud.get_user_by_email_and_password(email, password)
        if not user:
            return None

        return {"id": user[0], "email": user[1], "role": user[2]}

    def verify_user(self, email: str, code: str):
        user = self.user_crud.verify_user_code(email, code)
        if not user:
            return None

        self.user_crud.remove_user_code(email)
        return {"email": self.encrypter.decode(user[0]), "code": user[1], "role":user[2]}

    def change_password(self, email: str, old_password: str, new_password: str):
        user = self.user_crud.get_user_by_email_and_password(email, old_password)
        if not user:
            return None

        self.user_crud.change_user_password(email, new_password)
        return True

    def get_user_by_email(self, email: str):
        result = self.user_crud.get_user_by_email(email)
        if not result:
            return None

        return {"name": self.encrypter.decode(result[1]), "surname": self.encrypter.decode(result[2]), "email": self.encrypter.decode(result[3]), "role": result[4]}
