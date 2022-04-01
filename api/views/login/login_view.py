from typing import Optional
from pydantic import BaseModel

from api.models.blog import BlogStatus


class LoginRequest(BaseModel):
    email: str
    password: str