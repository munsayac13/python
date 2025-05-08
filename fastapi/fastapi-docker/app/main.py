from typing import Optional
from fastapi import FastAPI, Path, Body
from enum import Enum
from typing import Annotated
from pydantic import BaseModel, Field


app = FastAPI()

class ApostleName(str, Enum):
    john = "John"
    peter = "Peter"
    thomas = "Thomas"

@app.get("/")
async def read_root():
    return {"Apostles": "Disciples of Christ"}



@app.get("/apostles/{apostle_name}")
async def get_apostle(apostle_name: ApostleName):
    if apostle_name is ApostleName.john:
        return { "apostle_name": apostle_name, "message": "The WORD became flesh and dwelt among us"}

    if apostle_name is ApostleName.peter:
        return { "apostle_name": apostle_name, "message": "Before the rooster crows, you will deny me 3 times"}

    if apostle_name is ApostleName.thomas:
        return { "apostle_name": apostle_name, "message": "Doubting Thomas"}

    return {"model_name": apostle_name, "message": "{apostle_name} is not on the list of apostles"}
