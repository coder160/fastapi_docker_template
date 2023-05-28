from typing import Union
from fastapi import FastAPI 

api_fn = FastAPI()
#_server = SERVER


@api_fn.get("/")
def read_root():
    return {"Hello": "World"}


@api_fn.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"get_item_id": item_id, "get_q": q}

@api_fn.post("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"post_item_id": item_id, "post_q": q}
