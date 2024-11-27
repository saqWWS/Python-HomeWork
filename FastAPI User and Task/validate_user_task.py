from fastapi import HTTPException
from functools import wraps


def validator_for_task(func):
    @wraps(func)
    async def wrapper(new_task: dict, *args, **kwargs):
        title = new_task.get("title")
        description = new_task.get("description")

        if not isinstance(title, str) or not title.strip():
            raise HTTPException(status_code=400, detail="'Task' must be string, and non-empty string.")
        if not isinstance(description, str):
            raise HTTPException(status_code=400, detail="'Description' must be a non-empty string.")
        return await func(new_task=new_task, *args, **kwargs)

    return wrapper


def validator_for_user(func):
    @wraps(func)
    async def wrapper(user: dict, *args, **kwargs):
        min_length = 8
        contains_numbers = "0123456789"
        symbols = "~`!@#$%^&*()_-+={[}]|\\:;'<,>.?/"

        name = user.get("name")
        email = user.get("email")
        password = user.get("password")

        if not isinstance(name, str) or not name.strip():
            raise HTTPException(status_code=400, detail="Name must be a non-empty string.")
        if len(name) < 2:
            raise HTTPException(status_code=400, detail="Name must be longer than 2 characters.")
        if not name.isalpha():
            raise HTTPException(status_code=400, detail="Name must contain only alphabetic characters.")

        if not isinstance(email, str) or not email.strip():
            raise HTTPException(status_code=400, detail="Email must be a non-empty string.")
        if "@" and ".com" not in email:
            raise HTTPException(status_code=400, detail="Email must contain '@' and '.com'.")
        if len(email) <= 6:
            raise HTTPException(status_code=400, detail="Email must be longer than 6 characters.")

        if not isinstance(password, str) or not password.strip():
            raise HTTPException(status_code=400, detail="Password must be a non-empty string.")
        if len(password) < min_length:
            raise HTTPException(
                status_code=400,
                detail=f"Password must be at least {min_length} characters long."
            )
        if not any(num in contains_numbers for num in password):
            raise HTTPException(status_code=400, detail="Password must contain at least one number.")
        if not any(char in symbols for char in password):
            raise HTTPException(status_code=400, detail="Password must contain at least one special symbol.")

        return await func(user=user, *args, **kwargs)

    return wrapper
