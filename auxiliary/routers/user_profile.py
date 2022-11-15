from typing import List

from fastapi import APIRouter, status, Body, Depends
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from bson.json_util import ObjectId

import selectors_
import services_
import database
from schemas import (
    ListUserProfilesSchema, GetUserProfileSchema, CreateUserProfileRequestSchema, CreateUserProfileResponseSchema,
    UpdateUserProfileRequestSchema, UpdateUserProfileResponseSchema
)
from oauth2 import get_current_user


router = APIRouter(
    prefix='/user_profile',
    tags=['User profile']
)


@router.get('/', response_description="Get all user profiles",
            response_model=List[ListUserProfilesSchema])
async def list_user_profiles():
    user_profiles = await selectors_.list_user_profiles()
    if user_profiles:
        return user_profiles
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=f"something went wrong...")


@router.get('/{_id}', response_description="Get user profile", response_model=GetUserProfileSchema)
async def get_user_profile(user_id: str, current_user=Depends(get_current_user)):
    user_profile = await selectors_.get_user_profile(user_id)
    if user_profile:
        return user_profile
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=f"something went wrong...")


@router.post('/', response_description="Create user profile",
             response_model=CreateUserProfileResponseSchema)
async def create_user_profile(user_profile: CreateUserProfileRequestSchema = Body(...)):
    # hashing password
    import hashing
    user_profile.password = hashing.bcrypt(user_profile.password)
    user_profile = jsonable_encoder(user_profile)
    # performing create
    new_user_profile = await services_.create_user_profile(user_profile)
    created_user_profile = await database.user_profiles_collection.find_one({"_id": ObjectId(
        new_user_profile.inserted_id)})
    created_user_profile['_id'] = str(created_user_profile['_id'])

    # TODO: give condition
    from integration import create_user
    create_user(created_user_profile['_id'])

    return created_user_profile


@router.put("/{_id}", response_description="Update user profile",
            response_model=UpdateUserProfileResponseSchema)
async def update_user_profile(user_id: str, user_profile: UpdateUserProfileRequestSchema,
                              current_user=Depends(get_current_user)):
    user_profile = jsonable_encoder(user_profile)
    updated_user_profile = await services_.update_user_profile(user_id, user_profile)
    if updated_user_profile:
        return updated_user_profile
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=f"something went wrong...")


@router.delete("/{_id}", response_description="Delete user profile")
async def delete_user_profile(user_id: str, current_user=Depends(get_current_user)):
    is_deleted = await services_.delete_user_profile(user_id)
    if is_deleted:
        from integration import delete_user
        result, message = delete_user(user_id)
        return JSONResponse(content=f"Is deleted successfully = {result}, message = {message}")
    return JSONResponse(content=f"There is no object with such ID")
