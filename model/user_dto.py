from pydantic import BaseModel

class user_dto(BaseModel):
  user_name: str
  password: str