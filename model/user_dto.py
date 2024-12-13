from pydantic import BaseModel

class user_dto(BaseModel):
  email: str
  password: str

class user_code_dto(BaseModel):
  email: str
  code: str

class new_user_dto(BaseModel):
    email: str
    password: str
    name: str
    surname: str
    role: str

class new_password_dto(BaseModel):
    email: str
    old_password: str
    new_password: str

