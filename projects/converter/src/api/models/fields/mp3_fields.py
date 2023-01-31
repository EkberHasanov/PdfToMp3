from pydantic import Field

from src.api.utils.uuid_util import get_uuid

__all__ = ("MP3Fields",)


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
