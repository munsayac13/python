from fastapi import FastAPI
from enum import Enum


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

