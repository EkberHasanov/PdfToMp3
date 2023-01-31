from api.services.repositories.pdf_repository import PDFRepository
from api.services.repositories.mp3_repository import MP3Repository
from convert import to_mp3

pdf_repo = PDFRepository
mp3_repo = MP3Repository

def callback(channel, method, properties, body):
    error = to_mp3.start(body, pdf_repo, mp3_repo, channel)
    if error:
        channel.basic_nack(delivery_tag=method.delivery_tag)
    else:
        channel.basic_ack(delivery_tag=method.delivery_tag)
