"""Endpoints module."""

from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from api.containers import Container
from api.services import AuthorService

auth_route = APIRouter()


"""Endpoint authenticate author & generate JWT Token"""
@auth_route.post("/authenticate")
@inject
async def authenticate(author_service: AuthorService = Depends(Provide[Container.author_service]),):
    return None