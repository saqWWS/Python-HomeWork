from db import Session
from schemas import UserModel
from models import UserDB
import hashlib


def create_user(db: Session, user: UserModel):
    hash_password = hashlib.sha256(user.password.encode("utf-8", "ignore")).hexdigest()
    db_user = UserDB(username=user.username,
                     email=user.email,
                     password=hash_password,
                     full_name=user.full_name,
                     image_url=user.image_url,
                     is_admin=user.is_admin)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(UserDB).filter(UserDB.email == email).first()


def get_user_by_username(db: Session, username: str):
    return db.query(UserDB).filter(UserDB.username == username).first()


def update_user(db: Session, username: str, user: UserModel):
    db_user = db.query(UserDB).filter(UserDB.username == username).first()
    if db_user:
        db_user.username = user.username
        db_user.email = user.email
        db_user.full_name = user.full_name
        db_user.image_url = user.image_url
        db_user.is_admin = user.is_admin
        db.password = user.password
        # hashed_password = hashlib.sha256(user.password.encode("utf-8", "ignore")).hexdigest()
        # db_user.password = hashed_password

        db.commit()
        db.refresh(db_user)
        return db_user
    return None


def delete_user(db: Session, user_name: str):
    db_user = db.query(UserDB).filter(UserDB.username == user_name).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return None
