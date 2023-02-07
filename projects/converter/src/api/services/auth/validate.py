import os, requests
from flask.wrappers import Request

def verify_token(request: Request) -> tuple:
    if not "Authorization" in request.headers:
        print("You must provide Authorization")
        return None, ("missing authorization header", 401)

    token = request.headers["Authorization"]
    print(token)
    if not token:
        return None, ("missing credential token", 401)
    
    response = requests.post(
        "http://127.0.0.1/api/token/verify/",
        data={"token": token.split()[1]}
    )
    print(response.status_code, response.text)
    if response.status_code == 200:
        return response.text, None
    else:
        return None, (response.text, response.status_code)
