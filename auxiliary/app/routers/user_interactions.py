from fastapi import APIRouter, status, Depends
from starlette.responses import JSONResponse

import services_
import selectors_
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
        await services_.update_user_profile(user_to_unfollow['_id'], user_to_unfollow)
    except ValueError:
        return JSONResponse(content=f"Cannot unfollow")

    cur_user = await selectors_.get_user_profile(current_user.user_id)
    try:
        cur_user['following_ids'].remove(user_id)
        await services_.update_user_profile(cur_user['_id'], cur_user)
    except ValueError:
        return JSONResponse(content=f"Cannot unfollow")


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
        await services_.update_user_profile(user_to_unblock['_id'], user_to_unblock)
    except ValueError:
        return JSONResponse(content=f"Cannot unblock")

    cur_user = await selectors_.get_user_profile(current_user.user_id)
    try:
        cur_user['blocking_ids'].remove(user_id)
        await services_.update_user_profile(cur_user['_id'], cur_user)
    except ValueError:
        return JSONResponse(content=f"Cannot unblock")


@router.post('/users/{user_id}/favorite_posts/add/{post_id}',
             response_description='add post to favorites')
async def add_post_to_favorites(user_id: str, post_id: int):
    # TODO: does post with ID: post_id exist? is it worth checking?
    cur_user = await selectors_.get_user_profile(user_id)
    cur_user['favorite_posts_ids'].append(post_id)
    await services_.update_user_profile(cur_user['_id'], cur_user)


@router.post('/users/{user_id}/favorite_posts/remove/{post_id}',
             response_description='remove post from favorites')
async def remove_post_from_favorites(user_id: str, post_id: int):
    cur_user = await selectors_.get_user_profile(user_id)
    if not cur_user:
        return JSONResponse(content="User not found", status_code=status.HTTP_404_NOT_FOUND)
    try:
        cur_user['favorite_posts_ids'].remove(post_id)
        await services_.update_user_profile(cur_user['_id'], cur_user)
    except ValueError:
        return JSONResponse(content=f"Cannot remove from favorites")
    return JSONResponse(content=f"Removed successfully")