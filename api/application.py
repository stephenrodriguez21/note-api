"""Application module."""

from fastapi import FastAPI

from .containers import Container
from api.routes.authentication_routes import authentication_route
from api.routes.author_routes import author_route
from api.routes.blog_routes import blog_route
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    container = Container()

    db = container.db()

    # create schema. Migration to create tables.
    db.create_database()

    app = FastAPI()
    
    # enable CORS 
    app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

    # config IOC
    app.container = container

    # initialize all app routes
    app.include_router(authentication_route)
    app.include_router(author_route)
    app.include_router(blog_route)
    return app


app = create_app()
