from fastapi import APIRouter, status, Depends
from starlette.responses import JSONResponse

import services_
import selectors_
from oauth2 import get_current_user


router = APIRouter(
    prefix='/aux/user_interactions',
    tags=['User interactions']
)


@router.post('/follow/{username}', response_description="Follow user")
async def follow_user(username: str, current_user=Depends(get_current_user)):
    user_to_follow = await selectors_.get_user_profile(username)
    if not user_to_follow:
        return JSONResponse(content=f"User with username={username} not found", status_code=status.HTTP_404_NOT_FOUND)

    # user cannot follow himself/herself
    if current_user.username == username:
        return JSONResponse(content="You cannot follow yourself", status_code=status.HTTP_400_BAD_REQUEST)

    # if already followed
    if current_user.username in user_to_follow['followers']:
        return JSONResponse(content=f"Already followed to username={username}", status_code=status.HTTP_400_BAD_REQUEST)

    # if everything is ok do follow
    user_to_follow['followers'].append(current_user.username)
    await services_.update_user_profile(user_to_follow['username'], user_to_follow)

    cur_user = await selectors_.get_user_profile(current_user.username)
    cur_user['following'].append(username)
    await services_.update_user_profile(cur_user['username'], cur_user)

    return JSONResponse(content=f"Successfully done", status_code=status.HTTP_200_OK)


@router.post('/unfollow/{username}', response_description='Unfollow user')
async def unfollow_user(username: str, current_user=Depends(get_current_user)):
    user_to_unfollow = await selectors_.get_user_profile(username)
    if not user_to_unfollow:
        return JSONResponse(content=f"User with username={username} not found", status_code=status.HTTP_404_NOT_FOUND)
    try:
        user_to_unfollow['followers'].remove(current_user.username)
        await services_.update_user_profile(user_to_unfollow['username'], user_to_unfollow)
    except ValueError:
        return JSONResponse(content=f"Cannot unfollow")

    cur_user = await selectors_.get_user_profile(current_user.username)
    try:
        cur_user['following'].remove(username)
        await services_.update_user_profile(cur_user['username'], cur_user)
    except ValueError:
        return JSONResponse(content=f"Cannot unfollow")

    return JSONResponse(content=f"Successfully done", status_code=status.HTTP_200_OK)


@router.post('/block/{username}', response_description="Block user")
async def block_user(username: str, current_user=Depends(get_current_user)):
    user_to_block = await selectors_.get_user_profile(username)
    if not user_to_block:
        return JSONResponse(content=f"User with username={username} not found", status_code=status.HTTP_404_NOT_FOUND)

    # user cannot follow himself/herself
    if current_user.username == username:
        return JSONResponse(content=f"You cannot block yourself", status_code=status.HTTP_400_BAD_REQUEST)

    # check if already blocked
    if current_user.username in user_to_block['blockers']:
        return JSONResponse(content=f"Already blocked username={username}", status_code=status.HTTP_400_BAD_REQUEST)

    # if everything is ok do block
    user_to_block['blockers'].append(current_user.username)
    await services_.update_user_profile(user_to_block['username'], user_to_block)

    cur_user = await selectors_.get_user_profile(current_user.username)
    cur_user['blocking'].append(username)
    await services_.update_user_profile(cur_user['username'], cur_user)

    return JSONResponse(content=f"Successfully done", status_code=status.HTTP_200_OK)


@router.post('/unblock/{username}', response_description='Unblock user')
async def unblock_user(username: str, current_user=Depends(get_current_user)):
    user_to_unblock = await selectors_.get_user_profile(username)
    if not user_to_unblock:
        return JSONResponse(content=f"User with username={username} not found", status_code=status.HTTP_404_NOT_FOUND)
    try:
        user_to_unblock['blockers'].remove(current_user.username)
        await services_.update_user_profile(user_to_unblock['username'], user_to_unblock)
    except ValueError:
        return JSONResponse(content=f"Cannot unblock")

    cur_user = await selectors_.get_user_profile(current_user.username)
    try:
        cur_user['blocking'].remove(username)
        await services_.update_user_profile(cur_user['username'], cur_user)
    except ValueError:
        return JSONResponse(content=f"Cannot unblock")

    return JSONResponse(content=f"Successfully done", status_code=status.HTTP_200_OK)


@router.post('/users/{username}/favorite_posts/add/{post_id}',
             response_description='add post to favorites')
async def add_post_to_favorites(username: str, post_id: int):
    # TODO: does post with ID: post_id exist? is it worth checking?
    cur_user = await selectors_.get_user_profile(username)
    if post_id in cur_user['favorite_posts_ids']:
        return JSONResponse(content=f"This post is already added to favorites", status_code=status.HTTP_400_BAD_REQUEST)
    cur_user['favorite_posts_ids'].append(post_id)
    await services_.update_user_profile(cur_user['username'], cur_user)
    return JSONResponse(content=f"Successfully done", status_code=status.HTTP_200_OK)


@router.post('/users/{username}/favorite_posts/remove/{post_id}',
             response_description='remove post from favorites')
async def remove_post_from_favorites(username: str, post_id: int):
    cur_user = await selectors_.get_user_profile(username)
    if not cur_user:
        return JSONResponse(content="User not found", status_code=status.HTTP_404_NOT_FOUND)
    try:
        cur_user['favorite_posts_ids'].remove(post_id)
        await services_.update_user_profile(cur_user['username'], cur_user)
    except ValueError:
        return JSONResponse(content=f"Cannot remove from favorites")
    return JSONResponse(content=f"Removed successfully")
