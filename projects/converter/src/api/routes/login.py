from flask import Blueprint, request
from services.auth import access

api = Blueprint('api', __name__, url_prefix='/login')

@api.route("/", methods=["POST"]) # type: ignore
def login() -> None | tuple:
    token, error = access.login(request)

    if not error:
        return token
    else:
        return error
