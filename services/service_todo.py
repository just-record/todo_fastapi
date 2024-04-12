from sqlalchemy.orm import Session
from models.models import Todo
from schemas.schema_todo import TodoCreate


def create_todo(db: Session, todo: TodoCreate) -> Todo:
    try:
        db_todo = Todo(**dict(todo))
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return db_todo
    except Exception as e:
        db.rollback()
        print(f'Error: {e}')
        raise e


def get_todos(db: Session, skip: int = 0, limit: int = 100) -> list[Todo]:
    try:
        return db.query(Todo).offset(skip).limit(limit).all()
    except Exception as e:
        print(f'Error: {e}')
        raise e


def get_todo_by_id(db: Session, todo_id: int) -> Todo:
    try:
        return db.query(Todo).filter(Todo.id == todo_id).first()
    except Exception as e:
        print(f'Error: {e}')
        raise e


def get_todos_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> list[Todo]:
    try:
        return db.query(Todo).filter(Todo.user_id == user_id).offset(skip).limit(limit).all()
    except Exception as e:
        print(f'Error: {e}')
        raise e


def get_todos_with_filter(db: Session, skip: int = 0, limit: int = 100, completed: bool = False) -> list[Todo]:
    try:
        return db.query(Todo).filter(Todo.completed == completed).offset(skip).limit(limit).all()
    except Exception as e:
        print(f'Error: {e}')
        raise e


def get_todos_by_user_with_filter(db: Session, user_id: int, skip: int = 0, limit: int = 100, completed: bool = False) -> list[Todo]:
    try:
        return db.query(Todo).filter(Todo.user_id == user_id, Todo.completed == completed).offset(skip).limit(limit).all()
    except Exception as e:
        print(f'Error: {e}')
        raise e
    

def update_todo(db: Session, todo_id: int, todo: TodoCreate) -> Todo:
    try:
        db_todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == todo.user_id).first()    
        if not db_todo:
            raise Exception('요청한 Todo가 존재하지 않습니다. 본인이 작성한 Todo인지 확인해주세요.')
        for key, value in dict(todo).items():
            setattr(db_todo, key, value)
        db.commit()
        db.refresh(db_todo)
        return db_todo
    except Exception as e:
        db.rollback()
        print(f'Error: {e}')
        raise e


def update_todo_status(db: Session, todo_id: int, completed: bool, user_id: int) -> Todo:
    try:
        db_todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == user_id).first()
        if not db_todo:
            raise Exception('요청한 Todo가 존재하지 않습니다. 본인이 작성한 Todo인지 확인해주세요.')
        db_todo.completed = completed
        db.commit()
        db.refresh(db_todo)
        return db_todo
    except Exception as e:
        db.rollback()
        print(f'Error: {e}')
        raise e


def delete_todo(db: Session, todo_id: int, user_id: int) -> None:
    try:
        db_todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == user_id).first()
        if not db_todo:
            raise Exception('요청한 Todo가 존재하지 않습니다. 본인이 작성한 Todo인지 확인해주세요.')
        db.delete(db_todo)
        db.commit()
        return None
    except Exception as e:
        db.rollback()
        print(f'Error: {e}')
        raise e