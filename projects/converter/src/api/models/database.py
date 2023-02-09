from pymongo import MongoClient
from pymongo.collection import Collection

from config import DevelopmentConfig

settings = DevelopmentConfig()

__all__ = ('client', 'pdf_collection')

client = MongoClient(host='0.0.0.0', port=27017, username='root', password='1234')
pdf_collection: Collection = client[settings.database][settings.pdf_collection]
mp3_collection: Collection = client[settings.database][settings.mp3_collection]
