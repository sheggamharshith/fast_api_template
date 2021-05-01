from fastapi import APIRouter
from .views import router as main_router

user_router = APIRouter()

user_router.include_router(main_router)


