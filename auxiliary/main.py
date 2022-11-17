from fastapi import (
    FastAPI
)

from routers import (
    user_profile, authentication, user_interactions, integration
)


app = FastAPI()
app.include_router(user_profile.router)
app.include_router(authentication.router)
app.include_router(user_interactions.router)
app.include_router(integration.router)
