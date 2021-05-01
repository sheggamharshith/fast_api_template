import sys
from fastapi import APIRouter,Depends,Body,Request
from typing import Optional,Dict

import time
import jwt

from core.db.crud import get_user_by_email
from core.main import BaseSettings

from .schemas import *

settings = BaseSettings()


router = APIRouter()


def token_response(token: str):
    return {
        "access_token": token
    }


def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algo)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(
            token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


@router.post("/auth/login", tags=["Authentication"])
async def user_login(request: Request,user: UserLoginSchema = Body(...)):
    if get_user_by_email(request.state.db,user.email):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }
