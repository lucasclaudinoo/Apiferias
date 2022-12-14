from bson import ObjectId
from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    email: str
    password: str
    project: str
    admin: bool

class UserSchemaUpdate(BaseModel):
    name: str
    email: str
    password: str
    project: str
    admin: bool