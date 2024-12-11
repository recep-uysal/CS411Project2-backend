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
