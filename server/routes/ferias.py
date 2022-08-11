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
    ferias_collection.insert_one(ferias.__dict__)
    return "Férias criada com sucesso"


@router.get("/list_all_ferias")
async def list_all_ferias():
    total_ferias = ferias_collection.find()
    all_ferias = []
    for ferias in total_ferias:
        ferias["_id"] = str(ferias["_id"])
        ferias["user_id"] = str(ferias["user_id"])
        all_ferias.append(ferias)
    return all_ferias


@router.get("/list_all_ferias_by_user")
async def list_all_ferias_user(user_id: str):
    all_ferias = ferias_collection.find({'user_id': ObjectId(user_id)})
    ferias_return = []
    for ferias in all_ferias:
        ferias["_id"] = str(ferias["_id"])
        ferias["user_id"] = str(ferias["user_id"])
        ferias_return.append(ferias)
    return ferias_return


@router.put("/update_ferias")
async def update_ferias(id: str, ferias: DataFerias):
    if not ferias_collection.find_one({"_id": ObjectId(id)}):
        return ("A férias não existe")
    ferias_collection.update_one({"_id": ObjectId(id)}, {
        "$set": ferias.__dict__})
    return "Férias atualizada com sucesso"


@router.put("/update_ferias_status")
async def approve_ferias(email: str, id: str, status: bool):
    user = user_collection.find_one(filter={"email": email})

    if not user and not user["admin"]:
        return "O usuario não tem permissão para aprovar férias"

    if not ferias_collection.find_one({"_id": ObjectId(id)}):
        return "A ferias não existe"

    response = {True: "Aprovado", False: "Reprovado"}

    ferias_collection.update_one({"_id": ObjectId(id)}, {
        "$set": {"status": response[status]}})

    return "O período de férias foi " + response[status].lower()


@router.delete("/delete_ferias")
async def delete_ferias(id: str):

    if not ferias_collection.find_one({"_id": ObjectId(id)}):
        return ("A ferias não existe")

    ferias_collection.delete_one({"_id": ObjectId(id)})
    return ("A ferias foi deletada")
