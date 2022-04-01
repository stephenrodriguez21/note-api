from typing import Optional
from pydantic import BaseModel

from api.models.blog import BlogStatus


class EditBlogRequest(BaseModel):
    name: str
    content: str
    status: Optional[BlogStatus]
    category_id: int