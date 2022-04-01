"""Services module."""

from typing import Iterator

from fastapi import HTTPException
from api.models.author import Author
from api.models.blog import Blog
from api.repositories import AuthorRepository, BlogRepository
from api.views.blog.blog_views import EditBlogRequest



class AuthorService:

    def __init__(self, author_repository: AuthorRepository) -> None:
        self._author_repository: AuthorRepository = author_repository

    def get_author(self, email: str) -> Author:
        return self._author_repository.get_by_email(email)

class BlogService:

    def __init__(self, blog_repository: BlogRepository) -> None:
        self._blog_repository: BlogRepository = blog_repository


    def get_blogs(self) -> Iterator[Blog]:
        return self._blog_repository.get_all()
    

    async def get_by_id(self, blog_id: int) -> Blog:
        blog: Blog = await self._blog_repository.get_one(blog_id)
        if not blog:
            raise HTTPException(status_code=404, detail="Item not found")
        return blog


    async def create_one(self, model: EditBlogRequest) -> Blog:
        blog = Blog(name=model.name, content=model.content, category_id=model.category_id, author_id=1)
        return await self._blog_repository.create_or_update_one(blog)
    

    async def update_one(self, blog_id: int, update_model: EditBlogRequest) -> Blog:
        blog: Blog = await self._blog_repository.get_one(blog_id)
        if not blog:
            raise HTTPException(status_code=404, detail="Item not found")
        
        blog_data = update_model.dict(exclude_unset=True)
        for key, value in blog_data.items():
            setattr(blog, key, value)
        return await self._blog_repository.create_or_update_one(blog)
