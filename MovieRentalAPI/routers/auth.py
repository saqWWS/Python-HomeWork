from fastapi import APIRouter, HTTPException, Depends
from models.schemas import UserModel
from utils.auth_utils import create_jwt_token
from fastapi.security import OAuth2PasswordRequestForm
from utils.file_handler import read_file_for_users, write_file_for_users, users_file

router = APIRouter()


@router.post("/auth/register")
def register_user(user: UserModel):
    users = read_file_for_users(users_file)

    for new_user in users:
        if new_user.get("email") == user.get("email") or new_user.get("username") == user.get("username"):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists.")
    hash_password = pwd_context.hash(user.get('password'))
    user = {"username": user["username"], "email": user["email"], "password": hash_password}

    users.append(user)

    write_file_for_users(users_file, users)

    return {"message": "User created successfully!"}


def authenticate_user(user: UserModel):
    users = read_file_for_users(users_file)
    current_user = None
    for new_user in users:
        if new_user["username"] == user["username"]:
            current_user = new_user
            break

    if not current_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return False

    return pwd_context.verify(user["password"], current_user["password"])


@router.post("/auth/login")
def login_user(user: UserModel):
    if not authenticate_user(user):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    auth_token = create_jwt_token({"sub": user.username})
    return {"auth_token": auth_token}
