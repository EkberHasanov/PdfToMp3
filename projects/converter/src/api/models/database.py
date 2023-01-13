from pymongo import MongoClient
from pymongo.collection import Collection

from src.config import dev_settings as settings

__all__ = ('client', 'collection')

client = MongoClient(settings.MONGODB_URI)
collection: Collection = client[settings.database][settings.collection]
