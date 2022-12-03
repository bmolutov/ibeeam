from typing import List
import logging

from fastapi import APIRouter, status, Body, Depends
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from bson.json_util import ObjectId

import services_
import selectors_
import database
from schemas.user_profile import (
    ListUserProfilesSchema, GetUserProfileSchema, CreateUserProfileRequestSchema, CreateUserProfileResponseSchema,
    UpdateUserProfileRequestSchema, UpdateUserProfileResponseSchema
)
from oauth2 import get_current_user


router = APIRouter(
    prefix='/aux/user_profile',
    tags=['User profile']
)


@router.get('/', response_description="Get all user profiles",
            response_model=List[ListUserProfilesSchema])
async def list_user_profiles():
    user_profiles = await selectors_.list_user_profiles()
    if user_profiles:
        return user_profiles
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=f"something went wrong...")


@router.get('/{username}', response_description="Get user profile", response_model=GetUserProfileSchema)
async def get_user_profile(username: str, current_user=Depends(get_current_user)):
    user_profile = await selectors_.get_user_profile(username)
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

    # check if user with the username already exists
    if await selectors_.get_user_profile(user_profile['username']):
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                            content=f"user with the give username already exists")

    # performing create
    await services_.create_user_profile(user_profile)
    created_user_profile = await database.user_profiles_collection.find_one({"username": user_profile['username']})
    created_user_profile['_id'] = str(created_user_profile['_id'])

    # TODO: give condition
    import os
    from integration import create_user
    is_deleted_sync, message = create_user(
        created_user_profile['username'],
        created_user_profile['password']
    )
    logging.info(is_deleted_sync, message)
    return created_user_profile


@router.put("/{username}", response_description="Update user profile",
            response_model=UpdateUserProfileResponseSchema)
async def update_user_profile(username: str, user_profile: UpdateUserProfileRequestSchema,
                              current_user=Depends(get_current_user)):
    user_profile = jsonable_encoder(user_profile)
    updated_user_profile = await services_.update_user_profile(username, user_profile)
    if updated_user_profile:
        return updated_user_profile
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=f"something went wrong...")


@router.delete("/{username}", response_description="Delete user profile")
async def delete_user_profile(username: str, current_user=Depends(get_current_user)):
    is_deleted = await services_.delete_user_profile(username)
    if is_deleted:
        # TODO: fix sync
        from integration import delete_user
        result, message = delete_user(username)
        logging.info(result, message)
        return JSONResponse(content=f"Is deleted successfully = {result}, message = {message}")
    return JSONResponse(content=f"There is no object with such ID")
