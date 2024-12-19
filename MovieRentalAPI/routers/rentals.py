from fastapi import APIRouter, Depends, HTTPException
from models.schemas import RentalModel
from utils.auth_utils import get_current_user
from utils.file_handler import read_file_for_rentals, write_file_for_rentals, rentals_file

router = APIRouter()


@router.get("/rentals")
def get_rental_history(user_name):
    films = read_file_for_rentals(rentals_file)

    user_rentals = []

    for film in films:
        if film["username"] == user_name:
            user_rentals.append({"movie_title": film["movie_title"], "rental_date": film["rental_date"]})

    if not user_rentals:
        return {"message": f"No rentals found for user: {user_name}"}

    return {"username": user_name, "rentals": user_rentals}


@router.post("/rentals")
def rent_movie(rental_film: RentalModel, user_name, film_name):
    movies = read_file_for_films("move.json")
    users = read_file_for_users("users.json")
    rentals = read_file_for_rentals(rentals_file)

    user = None
    for us_ in users:
        if us_["username"] == user_name:
            user = us_
            break
    if not user:
        raise ValueError("User not found")

    movie = None
    for mov_ in movies:
        if mov_["title"] == film_name:
            movie = mov_
            break

    if not movie:
        raise ValueError("Film not found")

    for rental in rentals:
        if rental["username"] == user_name and rental["movie_title"] == film_name:
            raise ValueError(f"User '{user_name}' has already rented the movie '{film_name}'.")

    rental_info = {"username": user["username"], "movie_title": movie["title"],
                   "data": datetime.utcnow().isoformat()}

    rentals.append(rental_info)

    write_file_for_rentals(rentals_file, rentals)

    return rental_info
