from models.crud.pdf_create import PDFCreate
from models.crud.pdf_read import PDFRead
from api.models.database import collection
from utils.uuid_util import get_uuid


class PDFRepository:
    @staticmethod
    def get(pdf_id: str) -> PDFRead:
        document = collection.find_one({"_id": pdf_id})
        if not document:
            raise Exception("Could not find PDF in database")
        return PDFRead(**document)
    
    @staticmethod
    def create(create: PDFCreate) -> PDFRead:
        document = create.dict()
        document["_id"] = get_uuid()

        result = collection.insert_one(document)

        return PDFRepository.get(result.inserted_id)

