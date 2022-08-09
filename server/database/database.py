import pymongo
from pymongo.server_api import ServerApi

client = pymongo.MongoClient("mongodb+srv://lucasclaudino:Walleeva123@cluster0.kb47d7p.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.user
