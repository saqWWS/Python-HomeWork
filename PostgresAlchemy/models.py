

from sqlalchemy.orm import validates
from sqlalchemy import Column, Integer, String, Text, Boolean
from fastapi import HTTPException, status
from db import BASE


class UserDB(BASE):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    full_name = Column(Text, nullable=False)
    image_url = Column(Text, nullable=True)
    is_admin = Column(Boolean, default=False)


@validates("username")
def validate_username(self, key, username):
    if len(username) <= 2:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username mast be loger thne 2")

    return username


@validates("email")
def validate_email(self, key, email):
    import re

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if not (re.fullmatch(regex, email)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email format.")

    return email


@validates("password")
def validate_password(self, key, password):
    import re

    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    pat = re.compile(regex)
    mat = re.search(pat, password)
    if len(password) <= 8:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Password must be at least 8 characters long.")
    if not mat:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid password format.")

    return password
