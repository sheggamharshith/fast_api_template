from .views import router
from fastapi import APIRouter


auth_router = APIRouter()

auth_router.include_router(router)