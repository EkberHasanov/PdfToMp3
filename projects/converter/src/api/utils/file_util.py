import os
from werkzeug.datastructures import FileStorage
from config import DevelopmentConfig

settings = DevelopmentConfig()

def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.split('.')[-1].lower() in settings.ALLOWED_EXTENSIONS

def file_save(file: FileStorage) -> str:
    
    print("Func called")
    file.save(f'/home/akbar/Desktop/pdf/{file.filename}')
    file_url = f'/home/akbar/Desktop/pdf/{file.filename}'
    return file_url
