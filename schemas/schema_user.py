from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    username: str
    fullname: str | None = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        # orm_mode = True
        model_config = ConfigDict(from_attributes=True)


class UserInDB(User):
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None        
