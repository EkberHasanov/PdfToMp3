import json, pika
from typing import Tuple
from api.models.crud.pdf.pdf_create import PDFCreate
from api.models.crud.pdf.pdf_read import PDFRead
from api.services.repositories.pdf_repository import PDFRepository


def upload(create: PDFCreate, channel, access: dict) -> Tuple | None:
    try:
        file_id: PDFRead = PDFRepository.create(create)
    except Exception as error:
        return "internal server error", 500
    message = {
        "pdf_file_id": file_id,
        "mp3_file_id": None,
        "username": access["user_id"],
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
        PDFRepository.delete(pdf_id=file_id._id)
        return "internal server error", 500
