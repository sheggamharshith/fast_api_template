import os 
import sys


from fastapi import Depends, FastAPI, Request, Response
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
 
from functools import lru_cache
from .settings.base import BaseSettings

from .db.database import SessionLocal

from apps.user.urls import user_router
from apps.auth.urls import auth_router

import time


import uvicorn

@lru_cache()
def get_settings():
    return BaseSettings()



settings = get_settings()

app = FastAPI()

#middle ware support
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    except Exception as e :
        print(e)
    finally:
        request.state.db.close()
    return response


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin)
                       for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app.include_router(user_router)
app.include_router(auth_router)
