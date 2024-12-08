# services/auth_service.py
from crud.user_crud import UserCRUD
from model.user_dto import new_user_dto

class AuthService:
    def __init__(self):
        self.user_crud = UserCRUD()

    def verify_user_credentials(self, email: str, password: str):
        # Fetch user from the database via CRUD layer
        user = self.user_crud.get_user_by_email_and_password(email, password)
        if not user:
            return None
        # You can add additional business logic here if needed
        return user

    def register_user(self, new_user: new_user_dto):
        # Check if the email is already registered
        existing_user = self.user_crud.get_user_by_email(new_user.email)
        if existing_user:
            raise ValueError("Email is already registered")

        # Add the user to the database
        self.user_crud.add_user(new_user)

    def authenticate_user(self, email: str, password: str):
        # Fetch user from the database
        user = self.user_crud.get_user_by_email_and_password(email, password)
        if not user:
            return None

        # Additional logic, like verifying password hash, can be added here.
        # For simplicity, we assume the password is stored in plaintext (not recommended for production).
        return {"id": user[0], "email": user[1], "role": user[2]}
