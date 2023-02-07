from api.models.crud.mp3.mp3_create import MP3Create
from api.models.crud.mp3.mp3_read import MP3Read
from api.models.database import mp3_collection
from api.utils.uuid_util import get_uuid


__all__ = ("MP3Repository",)


class MP3Repository:
    @staticmethod
    def get(mp3_id: str) -> MP3Read:
        document = mp3_collection.find_one({"_id": mp3_id})
        if not document: raise Exception("Could not find MP3 in database")
        return MP3Read(**document)

    @staticmethod
    def create(create: MP3Create) -> MP3Read:
        document = create.dict()
        document["_id"] = get_uuid()

        result = mp3_collection.insert_one(document)

        return MP3Repository.get(result.inserted_id)
    
    @staticmethod
    def delete(mp3_id: str) -> None:
        result = mp3_collection.delete_one({"_id": mp3_id})
        if not result.deleted_count: raise Exception("Could not find MP3 file in database")

