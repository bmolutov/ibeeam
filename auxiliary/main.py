from fastapi import (
    FastAPI, status, Body
)
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from bson.json_util import ObjectId

import database
from models import CreateGetUpdateUserProfile, ListUserProfile


app = FastAPI()


@app.get('/list_user_profiles', response_description="Get all user profiles", response_model=ListUserProfile)
async def list_user_profiles():
    user_profiles = await database.list_user_profiles()
    if user_profiles:
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(user_profiles))
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=f"something went wrong...")


@app.get('/get_user_profile/{user_id}', response_description="Get user profile",
         response_model=CreateGetUpdateUserProfile)
async def get_user_profile(user_id: str):
    user_profile = await database.get_user_profile(user_id)
    if user_profile:
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(user_profile))
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=f"something went wrong...")


@app.post('/create_user_profile', response_description="Create user profile", response_model=CreateGetUpdateUserProfile)
async def create_user_profile(user_profile: CreateGetUpdateUserProfile = Body(...)):
    user_profile = jsonable_encoder(user_profile)
    new_user_profile = await database.create_user_profile(user_profile)
    created_user_profile = await database.users_collection.find_one({"_id": ObjectId(new_user_profile.inserted_id)})
    created_user_profile['_id'] = str(created_user_profile['_id'])

    from integration import create_user
    create_user(created_user_profile['_id'])

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonable_encoder(created_user_profile))


@app.put("/update_user_profile/{user_id}", response_description="Update user profile",
         response_model=CreateGetUpdateUserProfile)
async def update_user_profile(user_id: str, user_profile: CreateGetUpdateUserProfile = Body(...)):
    user_profile = jsonable_encoder(user_profile)
    updated_user_profile = await database.update_user_profile(user_id, user_profile)
    print(updated_user_profile)
    if updated_user_profile:
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(updated_user_profile))
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=f"something went wrong...")


@app.delete("/delete_user_profile/{user_id}", response_description="Delete user profile", response_model=bool)
async def delete_user_profile(user_id: str):
    is_deleted = await database.delete_user_profile(user_id)
    if is_deleted:

        from integration import delete_user
        delete_user(user_id)

        return JSONResponse(status_code=status.HTTP_200_OK, content=f"successfully deleted")
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=f"something went wrong...")
