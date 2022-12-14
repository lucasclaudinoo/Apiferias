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
async def get_all_users():
    total_users = user_collection.find()
    all_users = []
    for users in total_users:
        users["_id"] = str(users["_id"])
        all_users.append(users)
    return all_users


@router.get("/list_user/{user_id}")
async def get_user(id: str):
    user = user_collection.find_one({"_id": ObjectId(id)})
    user["_id"] = str(user["_id"])
    return user


@router.put("/update_user/{user_id}")
async def update_user(id: str, user: UserSchemaUpdate):
    if not user_collection.find_one({"_id": ObjectId(id)}):
        return ("O usuario não existe")
    user_collection.update_one({"_id": ObjectId(id)}, {"$set": user.__dict__})
    return "Usuario atualizado com sucesso"
