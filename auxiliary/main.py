from typing import Union

from fastapi import FastAPI

from database import collection

app = FastAPI()


@app.get("/")
async def read_root():
    data = {
        'first_name': 'bega'
    }
    await collection.insert_one(data)
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
