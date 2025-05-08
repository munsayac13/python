from fastapi import FastAPI, Path, Body
from enum import Enum
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/users")
async def read_users():
    return [ "Rock", "IGI" ]

@app.get("/otherusers")
async def read_userstwo():
    #WONT WORK
    #return [ "DE Shaw", "IMC "] + read_users()

    return [ "DE Shaw", "IMC "]
    
#####################################

#class ApostleName(str, None): # ERROR
class ApostleName(str, Enum):
    john = "John"
    peter = "Peter"
    thomas = "Thomas"

@app.get("/apostles/{apostle_name}")
async def get_apostle(apostle_name: ApostleName):
    if apostle_name is ApostleName.john:
        return { "apostle_name": apostle_name, "message": "The WORD became flesh and dwelt among us"}
    
    if apostle_name is ApostleName.peter:
        return { "apostle_name": apostle_name, "message": "Before the rooster crows, you will deny me 3 times"}
    
    if apostle_name is ApostleName.thomas:
        return { "apostle_name": apostle_name, "message": "Doubting Thomas"}
    
    return {"model_name": apostle_name, "message": "{apostle_name} is not on the list of apostles"}


###########################################

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# http://127.0.0.1:8000/items/?skip=0&limit=5 returns all three items
# http://127.0.0.1:8000/items/?skip=1&limit=5 returns only two items
# http://127.0.0.1:8000/items/?skip=2&limit=5 returns only one item


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/items/{item_id}")
async def read_itemtwo(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q":q})
        return {"item_id": item_id, "q": q}
    if not short:
        item.update({"description": "Boolean is not short rather long"})
        return item
    return {"item_id": item_id}

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "Boolean is not short rather long"})
    return item

##############################################


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None

@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results

@app.put("/itemstwo/{item_id}")
async def update_itemtwo(
        item_id: int, 
        item: Item, 
        user: User, 
        importance: Annotated[int, Body()]
    ):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results


@app.put("/itemsthree/{item_id}")
async def update_itemthree(item_id: int, item: Annotated[Item, Body(embed=True)], user: Annotated[User, Body(embed=True)], importance: Annotated[int, Body()]):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results


#######################################

class ItemTwo(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None


@app.put("/itemsfour/{item_id}")
async def update_itemfour(item_id: int, item: Annotated[ItemTwo, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results

#Field works the same way as Query, Path and Body, it has all the same parameters, etc


