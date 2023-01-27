import pika
from src.config import dev_settings as settings

def connect() -> pika.BlockingConnection:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=settings.broker_host, port=settings.broker_port))
    
    return connection
