from fastapi import APIRouter

import selectors_

router = APIRouter(
    prefix='/aux/integration',
    tags=['Integration']
)


@router.get('/users/{username}/favorite_posts_ids',
            response_description='ONLY FOR INTEGRATION: list favorite posts ids')
async def add_post_to_favorites(username: str):
    cur_user = await selectors_.get_user_profile(username)
    result = {
        'ids': cur_user.get('favorite_posts_ids')
    }
    return result
