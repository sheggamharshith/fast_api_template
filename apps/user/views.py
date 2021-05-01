from fastapi import APIRouter,Request


# database
from core.db import crud, models, schemas
from typing import Any, List



router = APIRouter()


@router.get("/", response_model=List[schemas.User])
def read_users(
    request: Request,
    skip: int = 0,
    limit: int = 1,
) -> "Return User":
    """
    Return's  users.
    """
    users = crud.get_users(request.state.db, skip=skip, limit=limit)
    return users
