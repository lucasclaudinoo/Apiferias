from pydantic import BaseModel
from datetime import datetime


class DataFerias(BaseModel):
    data_inicio: str
    data_fim: str
    dias_utilizados: int
    dias_restantes: int
    status: str = "aguardando"
    created_at: datetime = datetime.now()

class DataFeriasUpdate(BaseModel):
    user_id: str
    data_inicio: str
    data_fim: str
    dias_utilizados: int
    dias_restantes: int
    status: str
