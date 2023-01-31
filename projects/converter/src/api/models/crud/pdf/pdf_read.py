from api.models.crud.pdf.pdf_create import PDFCreate
from api.models.fields.pdf_fields import PDFFields

__all__ = ("PDFRead",)


class PDFRead(PDFCreate):
    pdf_id: str = PDFFields.pdf_id

