"""Application module."""

from fastapi import FastAPI

from .containers import Container
from api.routes.authentication_routes import authentication_route
from api.routes.author_routes import author_route
from api.routes.blog_routes import blog_route



def create_app() -> FastAPI:
    container = Container()


    db = container.db()
    db.create_database()

    app = FastAPI()
    app.container = container
    app.include_router(authentication_route)
    app.include_router(author_route)
    app.include_router(blog_route)
    return app


app = create_app()
