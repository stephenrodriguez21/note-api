"""Application module."""

from fastapi import FastAPI

from .containers import Container
from .endpoints import router
from api.routes.auth_routes import auth_route



def create_app() -> FastAPI:
    container = Container()


    db = container.db()
    db.create_database()

    app = FastAPI()
    app.container = container
    app.include_router(router)
    app.include_router(auth_route)
    return app


app = create_app()
