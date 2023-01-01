from pydantic import Field

from utils.uuid_util import get_uuid

__all__ = ("PDFFields", "MP3Fields")


class PDFFields:
    pdf_id = Field(
        description="Unique identifier of this person in the database",
        example=get_uuid(),
        min_length=36,
        max_length=36
    )
    
    file = Field(
        description="PDF file was uploaded to the database"
    )


class MP3Fields:
    mp3_id = Field(
        description="Unique identifier of this person in the database",
        example=get_uuid(),
        min_length=36,
        max_length=36
    )
    
    file = Field(
        description="Mp3 file was converted from PDF file"
    )
