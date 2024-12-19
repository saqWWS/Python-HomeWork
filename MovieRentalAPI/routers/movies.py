from fastapi import APIRouter, Depends, HTTPException
from models.schemas import MovieModel
from utils.auth_utils import get_current_user
from utils.file_handler import read_file_for_films, write_file_for_films, films_file

router = APIRouter()


@router.get("/movies")
def get_movies():
    movies = read_file_for_films(films_file)
    return movies


@router.post("/movies")
def add_movie(film: MovieModel):
    movies = read_file_for_films(films_file)

    for new_move in movies:
        if new_move.get("title") == film.get("title"):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Film already exists.")

    movies.append(film)

    write_file_for_films(movies, film)

    return {"message": "Film created successfully!"}
