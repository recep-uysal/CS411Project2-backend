# login_router.py
from fastapi import APIRouter, HTTPException

from config.email_authenticator import send_verification_email
from model.user_dto import user_dto, user_code_dto
from services.auth_service import AuthService

login_router = APIRouter()
auth_service = AuthService()

@login_router.post("/checkCode")
def check_code(user: user_code_dto):
    result = auth_service.verify_user(user.email, user.code)
    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "user": result}


@login_router.post("/login")
def login(user: user_dto):
    authenticated_user = auth_service.authenticate_user(user.email, user.password)
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    send_verification_email(user.email)
    return {"message": "Login successful", "user": authenticated_user}
