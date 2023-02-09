from pydantic import Field

from api.utils.uuid_util import get_uuid

__all__ = ("PDFFields",)


class PDFFields:
    _id = Field(
        description="Unique identifier of this person in the database",
        example=get_uuid(),
        min_length=36,
        max_length=36
    )
    
    file = Field(
        description="PDF file was uploaded to the database"
    )
