"""Repositories module."""

from typing import Callable, Iterator
from contextlib import AbstractContextManager
from sqlalchemy.orm import Session, joinedload

from api.models.author import Author
from api.models.blog import Blog


class AuthorRepository:

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory


    """Get a Author by id"""
    async def get_by_id(self, author_id: int) -> Blog:
        with self.session_factory() as session:
            return session.query(Author).filter(Author.id == author_id).first()

    
    """Get a Author by email"""
    async def get_by_email(self, email: int) -> Blog:
        with self.session_factory() as session:
            return session.query(Author).filter(Author.email == email).first()

    
    """Create new author or update exisitng blog"""
    async def create_or_update_one(self, author: Author) -> Author:
        with self.session_factory() as session:
            session.add(author)
            session.commit()
            session.refresh(author)
            return author 


class BlogRepository:

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory


    """Get a list of all blogs joined with related tables(author, category)"""
    async def get_all(self) -> Iterator[Blog]:
        with self.session_factory() as session:
            return session.query(Blog).options(joinedload('category')).all()

    
    """Get a blog joined with related tables(author, category)"""
    async def get_one(self, blog_id: int) -> Blog:
        with self.session_factory() as session:
            return session.query(Blog).filter(Blog.id == blog_id).first() 


    """Create new blog or update exisitng blog"""
    async def create_or_update_one(self, blog: Blog) -> Blog:
        with self.session_factory() as session:
            session.add(blog)
            session.commit()
            session.refresh(blog)
            return blog             