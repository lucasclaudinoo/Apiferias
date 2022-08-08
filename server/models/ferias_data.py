import datetime
from pydantic import BaseModel

class Data_ferias(BaseModel):
    name: str
    email: str
    data_inicio: str
    data_fim: str
    dias_utilizados: int
    dias_restantes: int
    status: str
    created_at: datetime.now()
    