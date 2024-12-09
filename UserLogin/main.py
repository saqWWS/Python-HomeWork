from fastapi import FastAPI, HTTPException, Request, Form, status, Response, Cookie, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from users_db import register_user, authenticate_user
from fastapi.templating import Jinja2Templates
from auth import get_current_user
from users_db import write_logs
from dotenv import load_dotenv
from datetime import datetime
from typing import Annotated
import uvicorn
import time
import os

current_time = datetime.now()
sessions = {}
load_dotenv()

formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
templates = Jinja2Templates(directory='static/templates')

PORT = int(os.environ.get("PORT"))
HOST = os.environ.get("HOST")

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
async def get_reg_users(request: Request):
    return templates.TemplateResponse('register.html', {"request": request})


@app.post("/register")
async def register_user_form(username: str = Form(...), password: str = Form(...)):
    if not register_user(username=username, password=password):
        raise HTTPException(status_code=409, detail="User exists. Try again!")
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)


@app.post("/login")
async def login_user(response: Response, username: str = Form(...), password: str = Form(...)):
    if not authenticate_user(username, password):
        write_logs([{"event": "login failed", "username": username, "status": "unsuccess",
                     "timestamp": formatted_time}])
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

    sessions[username] = True
    redirect = RedirectResponse("/secure", status_code=status.HTTP_303_SEE_OTHER)
    redirect.set_cookie(key="username", value=username)
    write_logs([{"event": "login", "username": username, "status": "succes", "timestamp": formatted_time}])

    return redirect


def get_current_user(username: str = Cookie(None)):
    if not username or username not in sessions:
        raise HTTPException(status_code=401, detail="User not authenticated.")
    return username


@app.get("/secure")
async def secure_page(request: Request, username: str = Depends(get_current_user)):
    if username not in sessions:
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    return templates.TemplateResponse("secure.html", {"request": request, "username": username})


@app.get("/logout")
def logout_user(response: Response):
    response.delete_cookie("username")


if __name__ == "__main__":
    uvicorn.run('main:app', port=PORT, host=HOST, reload=True)
