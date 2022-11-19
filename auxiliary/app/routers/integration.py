from fastapi import APIRouter

import selectors_

router = APIRouter(
    prefix='/integration',
    tags=['Integration']
)


@router.get('/users/{user_id}/favorite_posts_ids',
            response_description='ONLY FOR INTEGRATION: list favorite posts ids')
async def add_post_to_favorites(user_id: str):
    cur_user = await selectors_.get_user_profile(user_id)
    result = {
        'ids': cur_user.get('favorite_posts_ids')
    }
    return result
