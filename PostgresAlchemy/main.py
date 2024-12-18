


from fastapi import FastAPI, HTTPException, Depends, status
from models import BASE
from db import engine, Session, get_db
from schemas import UserModel
import uvicorn
import crud

app = FastAPI()


@app.on_event("startup")
def startup():
    try:
        BASE.metadata.create_all(bind=engine)
        print("Tables are created successfully.")
    except Exception as e:
        print("An error occurred during table creation:", e)
        raise e


@app.get("/users/{username}", response_model=UserModel)
def get_user(name: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, name.username)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user


@app.post("/users", response_model=UserModel)
def create(user: UserModel, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email alrady exists.")
    return crud.create_user(db, user)


@app.put("/users/{username}", response_model=UserModel)
def update_user(username: str, user: UserModel, db: Session = Depends(get_db)):
    db_user = crud.update_user(db, username, user)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    return db_user


@app.delete("/users/{name}", response_model=UserModel)
def delete(name: str, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, name)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


if __name__ == "__main__":
    uvicorn.run("main:app", port=3001, reload=True)
