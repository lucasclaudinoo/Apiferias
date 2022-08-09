from fastapi import APIRouter
from server.database.database import db
from server.models.ferias_data import DataFerias
from bson import ObjectId

router = APIRouter()


@router.post("/create")
async def create_ferias(ferias: DataFerias, user_id: str):
    user = db["user"].find_one(filter={"_id": user_id})
    if user:
        user.user_id = ObjectId(user.user_id)
        return "Férias criado com sucesso com id: " +\
            str(db["ferias"].insert_one(ferias.__dict__).inserted_id)
    return "Usuário não existe"

@router.get("/get_ferias/{ferias_id}")
async def get_ferias(email: str):
    ferias = db["ferias"].find_one({"email": email})
    if not ferias:
        return ("A ferias não existe")
    if ferias["status"] == "aguardando":
        return ("A ferias ainda não foi aprovada")
    if not ferias["status"]:
        return ("A ferias não foi aprovada")
    return ("A ferias foi aprovada pode pegar suas malas!!!")


@router.delete("/delete_ferias/{ferias_id}")
async def delete_ferias(email: str):
    if not db["ferias"].find_one({"email": email}):
        return ("A ferias não existe")
    db["ferias"].delete_one({"email": email})
    return ("A ferias foi deletada")

@router.put("/aprove_ferias/{ferias_id}")
async def aprove_ferias(email: str, user_id: str):
    user = db["user"].find_one(filter={"_id": user_id})
    if user["admin"]:
        if not db["ferias"].find_one({"email": email}):
            return "A ferias não existe"
        db["ferias"].update_one({"email": email}, {"$set": {"status": True}})
        return "A ferias foi aprovada"
    return "Usuário sem permissão"