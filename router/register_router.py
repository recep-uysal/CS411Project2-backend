from fastapi import APIRouter, HTTPException
from model.user_dto import new_user_dto
from services.auth_service import AuthService

register_router = APIRouter()
auth_service = AuthService()

@register_router.post("/register")
def register_user(new_user: new_user_dto):
    try:
        auth_service.register_user(new_user)
        return {"message": "User registered successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
