from typing import Annotated
from fastapi import APIRouter, Depends, Response, status
from fastapi.responses import JSONResponse
from api.endpoints.auth import get_current_active_user
from db.utils import get_db
from sqlalchemy.orm import Session
from models.models import User
from schemas.schema_todo import Todo, TodoCreate
from services.service_todo import create_todo, get_todos_by_user_with_filter, update_todo, update_todo_status, delete_todo
import logging


logger = logging.getLogger(__name__)
router = APIRouter(prefix="/todos")


@router.post("/add_todo", status_code=status.HTTP_201_CREATED, response_model=Todo)
def add_todo(current_user: Annotated[User, Depends(get_current_active_user)], 
             todo: TodoCreate, 
             db: Session = Depends(get_db)) -> Todo:
    try:
        todo.user_id = current_user.id
        return create_todo(db=db, todo=todo)
    except Exception as e:
        logger.error(f'Error: {e}')
        return JSONResponse(
            content={"detail": str(e)}, 
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )        


@router.get("/get_todos", status_code=status.HTTP_200_OK, response_model=list[Todo])
def get_todos(current_user: Annotated[User, Depends(get_current_active_user)], 
              completed: bool = False,
              db: Session = Depends(get_db)) -> list[Todo]:
    try:
        results = get_todos_by_user_with_filter(db=db, user_id=current_user.id, completed=completed)
        # 만약 조회 결과가 없다면 204 No Content를 반환
        if not results:
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        return results
    except Exception as e:
        logger.error(f'Error: {e}')
        return JSONResponse(
            content={"detail": str(e)}, 
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@router.put("/edit_todo/{todo_id}", status_code=status.HTTP_200_OK, response_model=Todo)
def edit_todo(current_user: Annotated[User, Depends(get_current_active_user)], 
              todo: TodoCreate,
              todo_id: int,
              db: Session = Depends(get_db)) -> Todo:
    try:
        todo.user_id = current_user.id
        return update_todo(db=db, todo_id=todo_id, todo=todo)
    except Exception as e:
        logger.error(f'Error: {e}')
        return JSONResponse(
            content={"detail": str(e)}, 
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    


@router.patch("/edit_todo_status/{todo_id}", status_code=status.HTTP_200_OK, response_model=Todo)
def edit_todo_status(current_user: Annotated[User, Depends(get_current_active_user)], 
                       completed: bool,
                       todo_id: int,
                       db: Session = Depends(get_db)) -> Todo:
    try:
        return update_todo_status(db=db, todo_id=todo_id, completed=completed, user_id=current_user.id)
    except Exception as e:
        logger.error(f'Error: {e}')
        return JSONResponse(
            content={"detail": str(e)}, 
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@router.delete("/remove_todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_todo(current_user: Annotated[User, Depends(get_current_active_user)], 
                todo_id: int,
                db: Session = Depends(get_db)) -> None:
    try:
        delete_todo(db=db, todo_id=todo_id, user_id=current_user.id)
        return None
    except Exception as e:
        logger.error(f'Error: {e}')
        return JSONResponse(
            content={"detail": str(e)}, 
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
