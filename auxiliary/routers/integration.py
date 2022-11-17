from fastapi import APIRouter, status
from starlette.responses import JSONResponse

import selectors_
import services_


router = APIRouter(
    prefix='/integration',
    tags=['Integration']
)


@router.post('/users/{user_id}/favorite_posts/{post_id}',
             response_description='ONLY FOR INTEGRATION: remove post from favorites')
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
