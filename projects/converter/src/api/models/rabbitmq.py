import pika
from config import DevelopmentConfig

settings = DevelopmentConfig()
params = pika.URLParameters("http://127.0.0.1:5672/")


def connect() -> pika.BlockingConnection:
    connection = pika.BlockingConnection(params)
    
    return connection
