from bson import ObjectId
from fastapi import APIRouter
from server.database.database import db
from server.models.ferias_data import Data_ferias


router = APIRouter()


@router.post("/create")
async def create_ferias(ferias: Data_ferias):
    if db["ferias"].find_one({"email": ferias.email}):
        return "O email " + ferias.email + " já existe"
    return "Férias criado com sucesso com id: " +\
        str(db["ferias"].insert_one(ferias.__dict__).inserted_id)

@router.delete("/delete_ferias/{ferias_id}")
async def delete_ferias(ferias_id: str):
    if not db["ferias"].find_one({"_id": ObjectId(ferias_id)}):
        return ("A ferias não existe")
    db["ferias"].delete_one({"_id": ObjectId(ferias_id)})
    return ("A ferias foi deletada")
