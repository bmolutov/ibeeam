from fastapi import (
    FastAPI
)

from routers import user_profile, authentication


app = FastAPI()
app.include_router(user_profile.router)
app.include_router(authentication.router)
