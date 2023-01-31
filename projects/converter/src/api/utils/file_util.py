from werkzeug.datastructures import FileStorage
from src.config import dev_settings as settings


def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.split('.')[-1].lower() in settings.ALLOWED_EXTENSIONS

def file_save(file: FileStorage) -> str:
    
    file.save(f'uploads/{file.filename}')
    file_url = f'uploads/{file.filename}'
    return file_url
