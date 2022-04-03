"""Endpoints module."""
from typing import Dict
from werkzeug.security import check_password_hash
import jwt
import datetime

from fastapi import APIRouter, Depends, HTTPException
from dependency_injector.wiring import inject, Provide
from api.containers import Container
from api.models.author import Author
from api.services import AuthorService
from api.views.login.login_view import LoginRequest


authentication_route = APIRouter()


"""Endpoint authenticate author & generate JWT Token"""
@authentication_route.post("/authenticate")
@inject
async def authenticate(model: LoginRequest, author_service: AuthorService = Depends(Provide[Container.author_service]),):
    author: Author = await author_service.get_author(model.email)
    if not author:
        raise HTTPException(status_code=401, detail="Invalid login credentials.")

    if check_password_hash(author.hashed_password, model.password):
        # generates the JWT Token
        token: str = jwt.encode({
                        'id': author.id,
                        'name': author.name,
                        'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes = 840)
                    }, "secret_config", algorithm="HS256")
        
        loggedin_user: Dict = {
            "id": author.id,
            "name": author.name,
            "email": author.email
        }
        
        return {'token' : token, 'loggedin_user': loggedin_user}

    
    raise HTTPException(status_code=401, detail="Invalid login credentials.")