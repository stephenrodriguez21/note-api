"""Blog Endpoints module."""

from fastapi import APIRouter, Depends, HTTPException, Request
from dependency_injector.wiring import inject, Provide
from api.containers import Container
from api.helpers.authentication_helper import verify_token
from api.services import BlogService, ManageUserService
from api.views.blog.blog_views import EditBlogRequest



blog_route = APIRouter()


"""Endpoint to get list of all blogs"""
@blog_route.get("/blogs",)
@inject
async def get_blogs(
        blog_service: BlogService = Depends(Provide[Container.blog_service]),
):
    return await blog_service.get_blogs()



"""Endpoint to get a blog by id"""
@blog_route.get("/blogs/{id}", dependencies=[Depends(verify_token)],)
@inject
async def edit_blog(id: int, request: Request,
        blog_service: BlogService = Depends(Provide[Container.blog_service]),
        manageuser_service: ManageUserService = Depends(Provide[Container.manageuser_service]),
):
    if await manageuser_service.can_modify_blog(id, request) == False:
        raise HTTPException(status_code=401, detail="You are only allowed to edit your blog")

    return await blog_service.get_by_id(id)



"""Endpoint to create a new blog"""
@blog_route.post("/blogs", dependencies=[Depends(verify_token)],)
@inject
async def create_blog(create_model: EditBlogRequest,
        request: Request,
        blog_service: BlogService = Depends(Provide[Container.blog_service]),
        manageuser_service: ManageUserService = Depends(Provide[Container.manageuser_service]),
):
    create_model.author_id = await manageuser_service.get_current_user(request)
    return await blog_service.create_one(create_model)



"""Endpoint to update a blog"""
@blog_route.put("/blogs/{id}", dependencies=[Depends(verify_token)],)
@inject
async def update_blog(id: int, update_model: EditBlogRequest, 
        request: Request,
        blog_service: BlogService = Depends(Provide[Container.blog_service]),
        manageuser_service: ManageUserService = Depends(Provide[Container.manageuser_service]),
):
    if await manageuser_service.can_modify_blog(id, request) == False:
        raise HTTPException(status_code=401, detail="You are only allowed to modify your blog")
    return await blog_service.update_one(id, update_model)



"""Endpoint to delete a blog"""
@blog_route.delete("/blogs/{id}", dependencies=[Depends(verify_token)],)
@inject
async def delete_blog(id: int,
        request: Request,
        blog_service: BlogService = Depends(Provide[Container.blog_service]),
        manageuser_service: ManageUserService = Depends(Provide[Container.manageuser_service]),
):
    if await manageuser_service.can_modify_blog(id, request) == False:
        raise HTTPException(status_code=401, detail="You are only allowed to delete your blog")
    return await blog_service.delete_one(id)