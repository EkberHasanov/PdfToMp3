import json
from flask import Blueprint, request
from api.services.auth import access, validate
from api.services.converter import pdf_to_mp3
from api.models.crud.pdf_create import PDFCreate
from api.models.rabbitmq import connect
from api.utils.file_util import allowed_file, file_save
from src.config import dev_settings as settings

api = Blueprint('api', __name__,)
connection = connect()
channel = connection.channel()

@api.route("/login", methods=["GET", "POST"]) # type: ignore
def login() -> None | tuple:
    token, error = access.login(request)

    if not error:
        return token
    else:
        return error

@api.route("upload/", methods=["GET", "POST"]) # type: ignore
def upload() -> None | tuple:
    access, error = validate.verify_token(request)
    
    access = json.loads(access)

    if len(request.files) > 1 and len(request.files) < 1:
        return "Only one file required", 400

    pdf_file = request.files['pdf']
    if pdf_file and allowed_file(str(pdf_file.filename)):
        try:
            file_url = file_save(file=pdf_file)
            create = PDFCreate(file_url=file_url)
            error = pdf_to_mp3.upload(create=create, channel=channel, access=access)
            if error:
                return error
            return "File successfully uploaded", 200
        except Exception as e:
            return "Error uploading file", 500
    else:
        return "File format not supported, only pdf files are supported", 400

@api.route("/download", methods=["GET",]) # type: ignore
def download():
    ...
