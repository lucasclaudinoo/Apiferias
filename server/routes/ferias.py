from fastapi import APIRouter
from server.database.database import db
from server.models.ferias import DataFerias
from bson import ObjectId


router = APIRouter()
ferias_collection = db["ferias"]
user_collection = db["user"]


@router.post("/create")
async def create_ferias(ferias: DataFerias, email: str):
    user = user_collection.find_one(filter={'email': email})
    if not user:
        return "O usuario não existe"
    ferias.user_id = user["_id"]
    ferias_collection.insert_one(ferias.dict())
    return "Férias criada com sucesso"


@router.get("/list_all_ferias")
async def list_all_ferias():
    total_ferias = ferias_collection.find()
    total_ferias = [ferias for ferias in total_ferias]
    for ferias in total_ferias:
        ferias["_id"] = str(ferias["_id"])
        ferias["user_id"] = str(ferias["user_id"])
    return total_ferias


@router.get("list_all_ferias_user/{user_id}")
async def list_all_ferias_user(user_id: str):
    ferias = ferias_collection.find(filter={'user_id': ObjectId(user_id)})
    ferias = [ferias for ferias in ferias]
    for ferias in ferias:
        ferias["_id"] = str(ferias["_id"])
        ferias["user_id"] = str(ferias["user_id"])
    return ferias

@router.put("/approve_ferias/{ferias_id}")
async def approve_ferias(email: str, id: str):
    user = user_collection.find_one(filter={"email": email})
    if not user["admin"]:
        return ("O usuario não tem permissão para aprovar férias")
    if not ferias_collection.find_one({"_id": ObjectId(id)}):
        return ("A ferias não existe")
    ferias_collection.update_one({"_id": ObjectId(id)}, {
        "$set": {"status": True}})
    return ("A ferias foi aprovada")


@router.put("/reject_ferias/{ferias_id}")
async def reject_ferias(email: str, id: str):
    user = user_collection.find_one(filter={"email": email})
    if not user["admin"]:
        return ("O usuario não tem permissão para aprovar férias")
    if not ferias_collection.find_one({"_id": ObjectId(id)}):
        return ("A ferias não existe")
    ferias_collection.update_one({"_id": ObjectId(id)}, {
        "$set": {"status": False}})
    return ("A ferias foi rejeitada")


@router.delete("/delete_ferias/{ferias_id}")
async def delete_ferias(id: str):
    if not ferias_collection.find_one({"_id": ObjectId(id)}):
        return ("A ferias não existe")
    ferias_collection.delete_one({"_id": ObjectId(id)})
    return ("A ferias foi deletada")

