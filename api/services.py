"""Services module."""

from typing import Iterator
from urllib.request import Request

from fastapi import HTTPException, Header
from api.helpers.authentication_helper import verify_token
from api.models.author import Author
from api.models.blog import Blog
from api.repositories import AuthorRepository, BlogRepository
from api.views.author.author_views import CreateAuthorRequest
from api.views.blog.blog_views import EditBlogRequest
from api.views.login.login_view import TokenModel
from werkzeug.security import generate_password_hash
import jwt


class ManageUserService:

    def __init__(self, author_repository: AuthorRepository, blog_repository: BlogRepository) -> None:
        self._author_repository: AuthorRepository = author_repository
        self._blog_repository: BlogRepository = blog_repository


    """Checks if user has permission to modify blog"""
    async def can_modify_blog(self, blog_id, request: Request) -> bool:
        x_token: str = request.headers.get('x-token')
        data: TokenModel = jwt.decode(x_token, "secret_config", algorithms=["HS256"])
        
        blog: Blog = await self._blog_repository.get_one(blog_id)
        if not blog:
            raise HTTPException(status_code=404, detail="Item not found")
        
        return blog.author_id == data.get('id')

    """returns the current logged in user"""
    async def get_current_user(self, request: Request) -> bool:
        x_token: str = request.headers.get('x-token')
        data: TokenModel = jwt.decode(x_token, "secret_config", algorithms=["HS256"])
        token: TokenModel = TokenModel(**data)
        return token.id


class AuthorService:

    def __init__(self, author_repository: AuthorRepository) -> None:
        self._author_repository: AuthorRepository = author_repository

    async def get_author(self, email: str) -> Author:
        return await self._author_repository.get_by_email(email)
    
    async def create_one(self, model: CreateAuthorRequest) -> Blog:
        author = Author(name=model.name, email=model.email, hashed_password=generate_password_hash(model.password))
        return await self._author_repository.create_or_update_one(author)

class BlogService:

    def __init__(self, blog_repository: BlogRepository) -> None:
        self._blog_repository: BlogRepository = blog_repository


    async def get_blogs(self) -> Iterator[Blog]:
        return await self._blog_repository.get_all()
    

    async def get_by_id(self, blog_id: int) -> Blog:
        blog: Blog = await self._blog_repository.get_one(blog_id)
        if not blog:
            raise HTTPException(status_code=404, detail="Item not found")
        return blog


    async def create_one(self, model: EditBlogRequest) -> Blog:
        blog = Blog(name=model.name, content=model.content, category_id=model.category_id, author_id=model.author_id)
        return await self._blog_repository.create_or_update_one(blog)
    

    async def update_one(self, blog_id: int, update_model: EditBlogRequest) -> Blog:
        blog: Blog = await self._blog_repository.get_one(blog_id)
        if not blog:
            raise HTTPException(status_code=404, detail="Item not found")
        
        blog_data = update_model.dict(exclude_unset=True)
        for key, value in blog_data.items():
            setattr(blog, key, value)
        return await self._blog_repository.create_or_update_one(blog)
