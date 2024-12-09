from datetime import timedelta, datetime
import secrets
import jwt

SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"


def token_auth(load_data: dict, secret_key: str, algorithm: str, expires: int = 10):
    data = load_data.copy()
    token = jwt.encode(load_data, secret_key, algorithm)
    now = datetime.now() + timedelta(minutes=expires)

    data["exp"] = now
    return token


def verify(tkone: str):
    username = jwt.decode(tkone, SECRET_KEY, ALGORITHM)
    return username


data = {"username": "Alice", "user_id": 38}
token = token_auth(data, SECRET_KEY, ALGORITHM)
print(token)
print(verify(token))
