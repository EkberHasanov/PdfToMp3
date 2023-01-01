import json, pika
from models.crud.pdf_read import PDFRead

def upload(file: bytes, db: PDFRead, channel: pika.BaseConnection, access: dict) -> tuple:
    ...
