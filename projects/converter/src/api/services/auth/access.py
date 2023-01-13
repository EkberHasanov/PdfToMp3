import requests
from flask.wrappers import Request

def login(request: Request) -> tuple:
    auth = request.authorization
    print("This is a login request")
    print(auth)
    if not auth:
        return None, ("missing credentials", 401)
    
    response = requests.post(
        url="http://127.0.0.1/api/token/", 
        json={
            "username": auth.username,
            "password": auth.password,
            },
    )

    if response.status_code == 200:
        print("THere is successful authentication")
        return response.text, None
    else:
        return None, (response.text, response.status_code)
