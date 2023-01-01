import pydantic
from pdf_create import PDFCreate
from models.fields import PDFFields

__all__ = ("PDFRead",)


class PDFRead(PDFCreate):
    pdf_id: str = PDFFields.pdf_id
