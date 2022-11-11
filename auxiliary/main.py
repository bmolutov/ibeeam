from typing import Union

from fastapi import FastAPI, Depends
from requests import Session

from database import collection, database
import models

app = FastAPI()


@app.post('/user')
def create_user(request: models.UserProfile):
    return request
