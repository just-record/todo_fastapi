from contextvars import Token
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from services.service_user import get_user

router = APIRouter()

@router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    params_dict = {'username': form_data.username}
    user = get_user(params=params_dict)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
            )
    # user = UserInDB(**user_dict) # get_user 함수의 결과를 dict로 받았을 때

    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
            )

    access_token = create_access_token(
        # data={"sub": user.username}
        data={"sub": user.username}
    )
    # 'Bearer' 타입의 access_token을 반환
    return {"access_token": access_token, "token_type": "bearer"}