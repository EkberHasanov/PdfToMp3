import os, requests
from flask.wrappers import Request

def verify_token(request: Request) -> tuple:
    if not "Authorization" in request.headers:
        return None, ("missing authorization header", 401)

    token = request.headers["Authorization"]

    if not token:
        return None, ("missing credential token", 401)
    
    response = requests.post(
        f"http://{os.getenv('AUTH_SERVICE_ADRESS')}/api/token/verify/",
        headers={"Authorization": token}
    )

    if response.status_code == 200:
        return response.text, None
    else:
        return None, (response.text, response.status_code)
