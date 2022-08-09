from pydantic import BaseModel
from typing import List, Optional
from bson.objectid import ObjectId
from datetime import datetime


class Data_ferias(BaseModel):
    name: str
    email: str
    data_inicio: str
    data_fim: str
    dias_utilizados: int
    dias_restantes: int
    status: str = "aguardando"
    created_at: datetime = datetime.now()


    