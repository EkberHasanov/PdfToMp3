import json, pika
from api.models.crud.pdf_create import PDFCreate
from api.services.repositories.pdf_repository import PDFRepository
from werkzeug.datastructures import FileStorage

def upload(create: PDFCreate, channel: pika.BaseConnection, access: dict) -> tuple:
    try:
        file_id = PDFRepository.create(create)
    except Exception as error:
        return "internal server error", 500

    message = {
        "file_id": str(file_id),
        "mp3_file_id": None,
        "username": access["username"],
    }
