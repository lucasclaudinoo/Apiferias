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


@router.delete("/delete_user/{user_id}")
async def delete_user(id: str):
    if not user_collection.find_one({"_id": ObjectId(id)}):
        return "O usuario não existe"
    user_collection.delete_one({"_id": ObjectId(id)})
    return "Usuario deletado com sucesso"


@router.get("/get_reproveds_ferias")
async def get_reproveds_ferias():
    ferias = db["ferias"].find({"status": False})
    ferias = [ferias for ferias in ferias]
    for ferias in ferias:
        ferias["_id"] = str(ferias["_id"])
    return ferias


@router.get("/get_aproveds_ferias")
async def get_aproveds_ferias():
    ferias = db["ferias"].find({"status": True})
    ferias = [ferias for ferias in ferias]
    for ferias in ferias:
        ferias["_id"] = str(ferias["_id"])
    return ferias


@router.get("/list_ferias")
async def get_all_ferias():
    ferias = db["ferias"].find()
    ferias = [ferias for ferias in ferias]
    for ferias in ferias:
        ferias["_id"] = str(ferias["_id"])
    return ferias


@router.get("/get_ferias/{ferias_id}")
async def get_ferias(id: str):
    ferias = db["ferias"].find_one({"_id": ObjectId(id)})
    ferias["_id"] = str(ferias["_id"])
    return ferias


@router.put("/aprove_ferias/{ferias_id}")
async def aprove_ferias(email: str):
    if not db["ferias"].find_one({"email": email}):
        return "A ferias não existe"
    db["ferias"].update_one({"email": email}, {"$set": {"status": True}})
    return "A ferias foi aprovada"


@router.put("/reprove_ferias/{ferias_id}")
async def reprove_ferias(email: str):
    if not db["ferias"].find_one({"email": email}):
        return "A ferias não existe"
    db["ferias"].update_one({"email": email}, {"$set": {"status": False}})
    return "A ferias foi reprovada"
