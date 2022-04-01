from pydantic import BaseModel


class LoginRequest(BaseModel):
    email: str
    password: str

class TokenModel(BaseModel):
    id: str
    name: str