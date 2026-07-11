from fastapi import APIRouter, HTTPException
from uuid import UUID, uuid4
from app.database import users_db
from app.schemas import CreateUser, ReturnUser
 

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/",response_model=ReturnUser)
async def add_user(user_data:CreateUser):
    new_id = uuid4()

    new_user = {
        "id":new_id,
    "name":user_data.name,
    "email":user_data.email,
    "age":user_data.age
    }

    users_db.append(new_user)

    return new_user


@router.get("/",response_model=list[ReturnUser])
async def get_users():
    return users_db

@router.get("/count")
async def get_count():
    count = len(users_db)
    return {
    "total_users": count
    }

@router.get("/{user_id}",response_model=ReturnUser)
async def get_user(user_id:UUID):
    for user in users_db:
        if user["id"] == user_id:
            return user

    return HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}")
async def delete_user(user_id:UUID):
    for user in users_db:
        if user["id"] == user_id:
            return {"message":"User deleted","user":user}

    return HTTPException(status_code=404, detail="User not found")
