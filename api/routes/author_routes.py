from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from api.containers import Container
from api.services import AuthorService
from api.views.author.author_views import CreateAuthorRequest

author_route = APIRouter()


"""Endpoint to create author"""
@author_route.post("/author")
@inject
async def create_author(model: CreateAuthorRequest, author_service: AuthorService = Depends(Provide[Container.author_service]),):
    await author_service.create_one(model)
    return None