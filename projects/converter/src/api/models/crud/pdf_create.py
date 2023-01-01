from typing import Any
from models.base import BaseModel

__all__ = ("PDFCreate",)


class PDFCreate(BaseModel):
    file: Any
