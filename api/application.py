"""Application module."""

from fastapi import FastAPI
from .containers import Container

def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    db.create_database()

    app = FastAPI()
    app.container = container

    return app

app = create_app()
