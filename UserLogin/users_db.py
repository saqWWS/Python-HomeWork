from passlib.context import CryptContext
from dotenv import load_dotenv
import json
import os

load_dotenv()

USERS_FILE = os.getenv("USERS_FILE", "default_users.json")
LOGS_FILE = os.getenv("LOGS_FILE", "default_logs.json")

pwd_context = CryptContext(schemes="sha256_crypt")


def write_logs(log):
    try:
        with open(LOGS_FILE, mode="a") as file:
            json.dump(log, file, indent=2)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {e}")
    except json.JSONDecodeError as error:
        raise Exception(f"JSON decode error: {error}")


def users_json_file(user: dict):
    try:
        with open(USERS_FILE, mode="w") as file:
            json.dump(user, file, indent=2)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {e}")
    except json.JSONDecodeError as error:
        raise Exception(f"JSON decode error: {error}")


def read_users_file() -> dict:
    try:
        with open(USERS_FILE, mode="r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def register_user(username: str, password: str) -> bool:
    db_users = read_users_file()
    if username in db_users:
        return False
    db_users[username] = {"username": username, "password": hash_password(password)}
    users_json_file(db_users)
    return True


def authenticate_user(username: str, password: str) -> bool:
    db_users = read_users_file()
    user = db_users.get(username)
    if not user:
        return False

    return verify_password(password, user["password"])
