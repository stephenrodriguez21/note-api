from typing import Dict, Optional
from pydantic import BaseModel

from api.models.blog import Blog, BlogStatus


class EditBlogRequest(BaseModel):
    name: str
    content: str
    status: Optional[BlogStatus]
    category_id: int
    author_id: Optional[int]

class BlogListViewModel(BaseModel):
    id: str
    name: str
    content: str
    category: str
    author: str
    status: BlogStatus


    @classmethod
    def from_model(cls, blog: Blog):
        _raw_result: Dict = {
            "id": blog.id,
            "name": blog.name,
            "content": blog.content,
            "category": blog.category.name,
            "author": blog.author.name,
            "status": blog.status,
        }

        return _raw_result
        