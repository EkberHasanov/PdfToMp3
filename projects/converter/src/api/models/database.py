from pymongo import MongoClient
from pymongo.collection import Collection

from src.config import dev_settings as settings

__all__ = ('client', 'pdf_collection')

client = MongoClient(settings.MONGODB_URI)
pdf_collection: Collection = client[settings.database][settings.pdf_collection]
mp3_collection: Collection = client[settings.database][settings.mp3_collection]
