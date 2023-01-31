from api.models.crud.mp3.mp3_create import MP3Create
from api.models.fields.mp3_fields import MP3Fields

__all__ = ("MP3Read",)


class MP3Read(MP3Create):
    mp3_id: str = MP3Fields.mp3_id

