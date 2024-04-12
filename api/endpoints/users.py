from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.responses import JSONResponse
from api.endpoints.auth import get_current_active_user
from db.utils import get_db
from sqlalchemy.orm import Session
from schemas.schema_user import User, UserCreate
from services.service_user import get_user_by_name, create_user


router = APIRouter(prefix="/users")


@router.post("/add_user/", status_code=status.HTTP_201_CREATED, response_model=User)
def add_user(user: UserCreate, db: Annotated[Session, Depends(get_db)]):
    try:
        db_user = get_user_by_name(db, username=user.username)
        if db_user:
            # raise HTTPException(status_code=400, detail="User already registered")
            return Response(status_code=status.HTTP_400_BAD_REQUEST, content="User already registered")
        return create_user(db=db, user=user)
    except Exception as e:
        print(f'Error: {e}')
        return JSONResponse(
            content={"detail": str(e)}, 
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@router.post("/me/", status_code=status.HTTP_200_OK, response_model=User)
def get_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    try:
        return current_user
    except Exception as e:
        print(f'Error: {e}')
        return JSONResponse(
            content={"detail": str(e)}, 
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )