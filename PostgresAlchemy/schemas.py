


from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class UserModel(BaseModel):
    id: Optional[int] = None
    username: str = Field(..., min_length=2, max_length=70)
    password: str = Field(..., min_length=8)
    email: EmailStr
    full_name: Optional[str]
    image_url: Optional[str] = None
    is_admin: bool = False

    class Config:
        from_attributes = True
