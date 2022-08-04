from bson import ObjectId
from fastapi import APIRouter
from server.database.database import db
from server.models.user import UserSchema, UserSchemaUpdate


router = APIRouter()
user_collection = db["user"]


@router.post("/create")
async def create_user(user: UserSchema) -> str:
    if user_collection.find_one({"email": user.email}):
        return "O email " + user.email + " já existe"
    return "Usuario criado com sucesso com id: " +\
        str(user_collection.insert_one(user.__dict__).inserted_id)


@router.get("/get_users")
async def get_users():
    users = user_collection.find()
    users = [user for user in users]
    for user in users:
        user["_id"] = str(user["_id"])
    return users


@router.get("/list_user/{user_id}")
async def get_user(id: str):
    user = user_collection.find_one({"_id": ObjectId(id)})
    user["_id"] = str(user["_id"])
    return user


@router.delete("/delete_user/{user_id}")
async def delete_user(id: str):
    user_delete = user_collection.find_one({"_id": ObjectId(id)})
    if user_delete is None:
        return ("O usuario não existe")
    else:
        user_collection.delete_one({"_id": ObjectId(id)})
        return "Usuario deletado com sucesso"


@router.put("/update_user/{user_id}")
async def update_user(user: UserSchemaUpdate):
    user_update = user_collection.find_one({"_id": ObjectId(id)})
    if user_update is None:
        return ("O usuario não existe")
    else:
        user_collection.update_one({"_id": ObjectId(id)}, {
                                   "$set": user.__dict__})
        return "Usuario atualizado com sucesso"
