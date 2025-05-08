from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserIn(BaseModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    username: str
    password: str
    email: EmailStr

class UserOut(BaseModel):
    username: str
    email: EmailStr
    firstName: Optional[str] = None
    lastName: Optional[str] = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    if user.firstName == "" and user.lastName == "":
        user.firstName = "n/a"
        user.lastName = "n/a"
    return user

