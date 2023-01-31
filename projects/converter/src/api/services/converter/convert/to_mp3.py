import os, json, tempfile, pika
from bson.objectid import ObjectId
from api.services.repositories.mp3_repository import MP3Repository
from api.services.repositories.pdf_repository import PDFRepository

def start(message: str, pdf_repo: PDFRepository, mp3_repo: MP3Repository, channel):
    msg = json.loads(message)
    temp_file = tempfile.NamedTemporaryFile()
    out = pdf_repo.get(pdf_id=msg["pdf_file_id"])
    ...
