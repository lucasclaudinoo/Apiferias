from bson import ObjectId
from pydantic import BaseModel

class AdminSchema(BaseModel):
    name: str
    email: str
    password: str

class AdminSchemaUpdate(BaseModel):
    name: str
    email: str
    password: str
