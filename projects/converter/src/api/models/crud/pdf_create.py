from werkzeug.datastructures import FileStorage
from models.base import BaseModel

__all__ = ("PDFCreate",)


class PDFCreate(BaseModel):
    file: FileStorage
