from models.crud.pdf_create import PDFCreate
from models.crud.pdf_read import PDFRead
from utils.uuid_util import get_uuid


class PDFRepository:
    @staticmethod
    def get(pdf_id: str) -> PDFRead:
        ...
    
    @staticmethod
    def create(create: PDFCreate) -> PDFRead:
        ...
