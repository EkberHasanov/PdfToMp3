from api.models.crud.pdf.pdf_create import PDFCreate
from api.models.crud.pdf.pdf_read import PDFRead
from api.models.database import pdf_collection
from api.utils.uuid_util import get_uuid


__all__ = ('PDFRepository',)


class PDFRepository:
    @staticmethod
    def get(pdf_id: str) -> PDFRead:
        document = pdf_collection.find_one({"_id": pdf_id})
        if not document: raise Exception("Could not find PDF in database")
        return PDFRead(**document)
    
    @staticmethod
    def create(create: PDFCreate) -> PDFRead:
        print("Creating PDF function...")
        document = create.dict()
        document["_id"] = get_uuid()
        print(document)
        result = pdf_collection.insert_one(document)
        print(result)
        return PDFRepository.get(result.inserted_id)
    
    @staticmethod
    def delete(pdf_id: str) -> None:
        result = pdf_collection.delete_one({"_id": pdf_id})
        if not result.deleted_count: raise Exception("Could not find PDF file in database")

