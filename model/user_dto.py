from pydantic import BaseModel

class user_dto(BaseModel):
  email: str
  password: str

class new_user_dto(BaseModel):
    email: str
    password: str
    name: str
    surname: str
    role: str

class UserDtoForAdmin(BaseModel):
   id: str
   name: str
   surname: str
   email: str
   role: str