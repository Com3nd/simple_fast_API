from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float]


@app.post("/items/")
async def item_add(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price * (1+item.tax)
        item_dict.update({"price_with_tax": price_with_tax, "tax_amount": int(price_with_tax - price_with_tax)})
    return item_dict


@app.get("/")
async def home():
    return {"message": "Hello World"}


@app.get("/users/me")
async def users_me():
    return {"user_id": f"current user id"}


@app.get("/items/{item_id}")
async def items_show(item_id: int, search: str = None):
    return {"items": f"{item_id} {search}"}


@app.get("/users/{user_id}")
async def user_read(user_id: int):
    return {"user_id": f"{user_id}"}


# @app.
#   get()
#   post()
#   put()
#   patch()
#   delete()
#   option()
#   head()
#   trace()

