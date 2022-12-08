from fastapi import (
    FastAPI
)
from fastapi.middleware.cors import CORSMiddleware

from routers import (
    user_profile, authentication, user_interactions, integration
)


app = FastAPI(
    title="Ibeeam",
    version="0.0.1",
    docs_url="/aux/docs",
    redoc_url="/aux/redoc",
    openapi_url="/aux/openapi.json",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_profile.router)
app.include_router(authentication.router)
app.include_router(user_interactions.router)
app.include_router(integration.router)
