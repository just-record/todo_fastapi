from sqlalchemy.orm import Session
from models.models import Todo
from schemas.schema_todo import TodoCreate


def create_todo(db: Session, todo: TodoCreate) -> Todo:
    db_todo = Todo(**dict(todo))
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def get_todos(db: Session, skip: int = 0, limit: int = 100) -> list[Todo]:
    return db.query(Todo).offset(skip).limit(limit).all()


def get_todo_by_id(db: Session, todo_id: int) -> Todo:
    return db.query(Todo).filter(Todo.id == todo_id).first()


def get_todos_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> list[Todo]:
    return db.query(Todo).filter(Todo.user_id == user_id).offset(skip).limit(limit).all()


def get_todos_with_filter(db: Session, skip: int = 0, limit: int = 100, completed: bool = False) -> list[Todo]:
    return db.query(Todo).filter(Todo.completed == completed).offset(skip).limit(limit).all()


def get_todos_by_user_with_filter(db: Session, user_id: int, skip: int = 0, limit: int = 100, completed: bool = False) -> list[Todo]:
    return db.query(Todo).filter(Todo.user_id == user_id, Todo.completed == completed).offset(skip).limit(limit).all()


def update_todo(db: Session, todo_id: int, todo: TodoCreate) -> Todo:
    db_todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == todo.user_id).first()    
    for key, value in dict(todo).items():
        setattr(db_todo, key, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def update_todo_status(db: Session, todo_id: int, completed: bool, user_id: int) -> Todo:
    db_todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == user_id).first()
    db_todo.completed = completed
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, todo_id: int, user_id: int) -> None:
    db_todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == user_id).first()
    db.delete(db_todo)
    db.commit()
    return None


