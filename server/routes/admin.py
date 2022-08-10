from bson import ObjectId
from fastapi import APIRouter
from server.database.database import db

router = APIRouter()
user_collection = db["user"]


@router.get("/get_admin")
async def verify_admin(id: str):
    user = user_collection.find_one({"_id": ObjectId(id)})
    if not user:
        return "O usuario não existe"
    if not user["admin"]:
        return "O usuario não é administrador"
    return "O usuario é administrador"


@router.delete("/delete_user")
async def delete_user(id: str):
    if not user_collection.find_one({"_id": ObjectId(id)}):
        return "O usuario não existe"
    user_collection.delete_one({"_id": ObjectId(id)})
    return "Usuario deletado com sucesso"
