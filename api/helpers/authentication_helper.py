from fastapi import Depends, HTTPException, Header
from dependency_injector.wiring import inject, Provide
from api.containers import Container

from api.services import AuthorService


@inject
async def verify_token(x_token: str = Header(...), author_service: AuthorService = Depends(Provide[Container.author_service])):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")