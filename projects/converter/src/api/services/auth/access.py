import os, requests
from flask.wrappers import Request

def login(request: Request) -> tuple:
    auth = request.authorization
    if not auth:
        return None, ("missing credentials", 401)
    
    basicAuth = (auth.username, auth.password)

    response = requests.post(
        f"http://{os.getenv('AUTH_SERVICE_ADRESS')}/api/token/", auth=basicAuth, #type: ignore
    )

    if response.status_code == 200:
        return response.text, None
    else:
        return None, (response.text, response.status_code)
