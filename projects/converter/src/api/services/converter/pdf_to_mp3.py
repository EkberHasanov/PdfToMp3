import json, pika
from typing import Tuple
from api.models.crud.pdf_create import PDFCreate
from api.models.crud.pdf_read import PDFRead
from api.services.repositories.pdf_repository import PDFRepository


def upload(create: PDFCreate, channel, access: dict) -> Tuple | None:
    try:
        file_id: PDFRead = PDFRepository.create(create)
    except Exception as error:
        return "internal server error", 500

    message = {
        "file_id": str(file_id),
        "mp3_file_id": None,
        "username": access["username"],
    }
    try:
        channel.basic_publish(
            exchange="",
            routing_key="pdf",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE, # type: ignore
            ),
        )
    except Exception as error:
        PDFRepository.delete(pdf_id=file_id.pdf_id)
        return "internal server error", 500
