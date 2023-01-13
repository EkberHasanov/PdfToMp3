from flask import Blueprint, request
from api.services.auth import access

api = Blueprint('api', __name__,)

@api.route("/login", methods=["GET", "POST"]) # type: ignore
def login() -> None | tuple:
    token, error = access.login(request)

    if not error:
        return token
    else:
        return error
