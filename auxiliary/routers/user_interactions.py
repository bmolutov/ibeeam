from fastapi import APIRouter, status, Depends
from starlette.responses import JSONResponse

import selectors_
import services_
from oauth2 import get_current_user


router = APIRouter(
    prefix='/user_interactions',
    tags=['User interactions']
)


@router.post('/follow/{_id}', response_description="Follow user")
async def follow_user(user_id: str, current_user=Depends(get_current_user)):
    user_to_follow = await selectors_.get_user_profile(user_id)
    if not user_to_follow:
        return JSONResponse(content=f"User with ID={user_id} not found", status_code=status.HTTP_404_NOT_FOUND)
    user_to_follow['followers_ids'].append(current_user.user_id)
    await services_.update_user_profile(user_to_follow['_id'], user_to_follow)

    cur_user = await selectors_.get_user_profile(current_user.user_id)
    cur_user['following_ids'].append(user_id)
    await services_.update_user_profile(cur_user['_id'], cur_user)


@router.post('/unfollow/{_id}', response_description='Unfollow user')
async def unfollow_user(user_id: str, current_user=Depends(get_current_user)):
    user_to_unfollow = await selectors_.get_user_profile(user_id)
    if not user_to_unfollow:
        return JSONResponse(content=f"User with ID={user_id} not found", status_code=status.HTTP_404_NOT_FOUND)
    try:
        user_to_unfollow['followers_ids'].remove(current_user.user_id)
    except ValueError:
        return JSONResponse(content=f"Cannot unfollow")
    await services_.update_user_profile(user_to_unfollow['_id'], user_to_unfollow)

    cur_user = await selectors_.get_user_profile(current_user.user_id)
    try:
        cur_user['following_ids'].remove(user_id)
    except ValueError:
        return JSONResponse(content=f"Cannot unfollow")
    await services_.update_user_profile(cur_user['_id'], cur_user)


@router.post('/block/{_id}', response_description="Block user")
async def block_user(user_id: str, current_user=Depends(get_current_user)):
    user_to_block = await selectors_.get_user_profile(user_id)
    if not user_to_block:
        return JSONResponse(content=f"User with ID={user_id} not found", status_code=status.HTTP_404_NOT_FOUND)
    user_to_block['blockers_ids'].append(current_user.user_id)
    await services_.update_user_profile(user_to_block['_id'], user_to_block)

    cur_user = await selectors_.get_user_profile(current_user.user_id)
    cur_user['blocking_ids'].append(user_id)
    await services_.update_user_profile(cur_user['_id'], cur_user)


@router.post('/unblock/{_id}', response_description='Unblock user')
async def unblock_user(user_id: str, current_user=Depends(get_current_user)):
    user_to_unblock = await selectors_.get_user_profile(user_id)
    if not user_to_unblock:
        return JSONResponse(content=f"User with ID={user_id} not found", status_code=status.HTTP_404_NOT_FOUND)
    try:
        user_to_unblock['blockers_ids'].remove(current_user.user_id)
    except ValueError:
        return JSONResponse(content=f"Cannot unblock")
    await services_.update_user_profile(user_to_unblock['_id'], user_to_unblock)

    cur_user = await selectors_.get_user_profile(current_user.user_id)
    try:
        cur_user['blocking_ids'].remove(user_id)
    except ValueError:
        return JSONResponse(content=f"Cannot unblock")
    await services_.update_user_profile(cur_user['_id'], cur_user)
