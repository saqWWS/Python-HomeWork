from fastapi import FastAPI
from dotenv import load_dotenv
from routers import auth, movies, rentals
import uvicorn
import os

load_dotenv()

USERS_FILE = os.getenv("USERS_FILE")
MOVIES_FILE = os.getenv("MOVIES_FILE")
RENTALS_FILE = os.getenv("RENTALS_FILE")

HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8090))

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(movies.router, prefix="/movies", tags=["Movies"])
app.include_router(rentals.router, prefix="/rentals", tags=["Rentals"])

if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
