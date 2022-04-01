from pydantic import BaseModel


class CreateAuthorRequest(BaseModel):
    name: str
    email: str
    password: str