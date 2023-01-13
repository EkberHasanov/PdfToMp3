import json
from flask import Blueprint, request
from api.services.auth import access, validate
from api.services.converter import pdf_to_mp3
from api.models.crud.pdf_create import PDFCreate

api = Blueprint('api', __name__,)

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
    
    for _, file in request.files.items():
        create = PDFCreate(file=file)
        error = pdf_to_mp3.upload(create=create, channel="...", access=access) # type: ignore TODO: create rabbitmq connection

        if error:
            return error
    
    return "success", 200

@api.route("/download", methods=["GET",]) # type: ignore
def download():
    ...
