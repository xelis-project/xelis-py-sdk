import base64

def createBasicAuthToken(username: str, password: str):
    auth = "{}:{}".format(username, password)
    data = base64.b64encode(auth.encode())
    token = data.decode()
    return "Basic {}".format(token)
