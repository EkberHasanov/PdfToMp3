import os, requests, jwt
from flask.wrappers import Request

def decode_jwt_token(token):
    try:
        decoded_token = jwt.decode(token, "django-insecure-!^93m5qqt3j#fwf-^3+0t#gu*xy6^3lk^2^1e8rk+&87l!fgkx", algorithms=['HS256'])
        print(decoded_token)
        return decoded_token
    except jwt.exceptions.DecodeError:
        return None

def verify_token(request: Request) -> tuple:
    if not "Authorization" in request.headers:
        return None, ("missing authorization header", 401)

    token = request.headers["Authorization"].split()[1]
    if not token:
        return None, ("missing credential token", 401)
    
    response = requests.post(
        "http://127.0.0.1/api/token/verify/",
        data={"token": token}
    )
    decoded_token = decode_jwt_token(token=token)
    print(response.status_code, decoded_token)
    if response.status_code == 200:
        return decoded_token, None
    else:
        return None, (response.text, response.status_code)
