import os, json, pika
from api.models.crud.mp3.mp3_create import MP3Create
from api.services.converter.convert.services import generate_audio, read_pdf_content
from api.services.repositories.mp3_repository import MP3Repository
from api.services.repositories.pdf_repository import PDFRepository
from api.utils.uuid_util import get_uuid

async def start(message: str, pdf_repo: PDFRepository, mp3_repo: MP3Repository, channel):
    msg = json.loads(message)
    file_url = pdf_repo.get(pdf_id=msg["pdf_file_id"]).file_url
    pdf_content = read_pdf_content(file_url=file_url)
    await generate_audio(text=pdf_content, file_name=msg["pdf_file_id"])
    pdf_repo.delete(pdf_id=msg["pdf_file_id"])
    os.remove(file_url)
    mp3_file = mp3_repo.create(create=MP3Create(file_url=f"uploads/{get_uuid()}"))
    msg["mp3_file_id"] = mp3_file.mp3_id
    
    try:
        channel.basic_publish(
            exchange="",
            routing_key="mp3",
            body=json.dumps(msg),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE # type: ignore
            ),
        )
    except Exception as error:
        mp3_repo.delete(mp3_id=mp3_file.mp3_id)
        return f"Failed to publish the message: {error}"
