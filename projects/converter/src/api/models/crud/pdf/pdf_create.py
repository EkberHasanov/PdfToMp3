from api.models.base import BaseModel

__all__ = ("PDFCreate",)


class PDFCreate(BaseModel):
    file_url: str
