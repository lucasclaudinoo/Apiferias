from tkinter.font import BOLD
from bson import ObjectId
from fastapi import APIRouter
from server.database.database import db
from server.models.user import UserSchema, UserSchemaUpdate


router = APIRouter()
user_collection = db["user"]

@router.get("/admin/get_admin")
async def verify_admin(id: str):
    if not user_collection.find_one({"_id": ObjectId(id)}):
        return ("O usuario não existe")
    if user_collection.find_one({"_id": ObjectId(id)})["admin"] == False:
        return ("O usuario não é administrador")
    user_collection.find_one({"_id": ObjectId(id)})["admin"] ==  True
    return ("O usuario é administrador")

@router.delete("/delete_user/{user_id}")
async def delete_user(id: str):
    if not user_collection.find_one({"_id": ObjectId(id)}):
        return ("O usuario não existe")
    user_collection.delete_one({"_id": ObjectId(id)})
    return ("Usuario deletado com sucesso")



