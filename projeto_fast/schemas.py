from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str

class UserSchema(BaseModel):
    username: str
    email: EmailStr
    passeord: str

class UserPublic(BaseModel):
    username: str
    email: EmailStr