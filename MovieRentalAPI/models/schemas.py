from pydantic import BaseModel, Field, EmailStr
from datetime import timedelta


class UserModel(BaseModel):
    username: str = Field(..., min_length=2, max_length=70)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=70)


class MovieModel(BaseModel):
    title: str = Field(..., min_length=3, max_length=55)
    genre: str = Field(..., min_length=3, max_length=55)
    rating: float = Field(..., ge=0.0, le=10.0)


class RentalModel(BaseModel):
    user: str
    movie: str
    rental_duration: timedelta = Field(..., description="Rental as a timedelta")
