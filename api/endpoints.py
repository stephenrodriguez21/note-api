"""Endpoints module."""

from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from api.containers import Container
from api.helpers.authentication_helper import verify_token
from api.services import BlogService
from api.views.blog.blog_views import EditBlogRequest



router = APIRouter()


"""Endpoint to get list of all blogs"""
@router.get("/blogs")
@inject
def get_blogs(
        blog_service: BlogService = Depends(Provide[Container.blog_service]),
):
    return blog_service.get_blogs()


"""Endpoint to get a blog by id"""
@router.get("/blogs/{id}", dependencies=[Depends(verify_token),])
@inject
async def edit_blog(id: int,
        blog_service: BlogService = Depends(Provide[Container.blog_service]),
):
    return await blog_service.get_by_id(id)


"""Endpoint to create a new blog"""
@router.post("/blogs")
@inject
async def create_blog(create_model: EditBlogRequest, blog_service: BlogService = Depends(Provide[Container.blog_service]),):
    return await blog_service.create_one(create_model)


"""Endpoint to update a blog"""
@router.put("/blogs/{id}")
@inject
async def update_blog(id: int, update_model: EditBlogRequest, blog_service: BlogService = Depends(Provide[Container.blog_service])):
    return await blog_service.update_one(id, update_model)