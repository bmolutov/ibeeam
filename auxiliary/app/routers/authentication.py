from datetime import timedelta

from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from schemas import GetUserProfileSchema
import selectors_
from hashing import verify
from token_ import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token


router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
async def login(request: OAuth2PasswordRequestForm = Depends()):
    user_profile = await selectors_.get_user_profile(request.username)
    if not user_profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid user_id"
        )
    if not verify(user_profile['password'], request.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Incorrect password"
        )

    # generate a jwt token and return it
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(GetUserProfileSchema(**user_profile).id)}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
