from file_read import read_file_for_users, read_file_for_tasks, write_file_for_users, write_file_for_tasks
from validate_user_task import validator_for_user, validator_for_task
from fastapi import FastAPI, Body, HTTPException
from error import FileError, NotFoundError
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()
app = FastAPI()

USERS_FILE = os.getenv("USERS_FILE", "default_users.json")
TASKS_FILE = os.getenv("TASKS_FILE", "default_tasks.json")
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8090))

users_file = "users.json"
tasks_file = "tasks.json"


@app.get("/users")
async def get_users():
    """
       Retrieves all users from the JSON file.

       Returns:
       - list: A list of user dictionaries or an error message if an error occurs.
       """

    try:
        all_users = await read_file_for_users(users_file)
        if len(all_users) == 0:
            return []
        else:
            return all_users
    except FileError as e:
        return {"error": str(e)}


@app.get("/users/{user_id}")
async def get_user_by_id(user_id: int):
    """
       Retrieves a user by their unique ID.

       Parameters:
       - user_id (int): The unique ID of the user to be retrieved.

       Returns:
       - dict: The user data if found, or an error message if not found.
       """

    try:
        users = await read_file_for_users(users_file)
        for user in users:
            if user["id"] == user_id:
                return user
                break
        raise NotFoundError(f"User with id {user_id} not found.")
    except FileError as e:
        return {"error": str(e)}


@app.post("/users/register")
@validator_for_user
async def create_new_user(user: dict):
    """
      Registers a new user by validating the user data, checking if the user exists, and saving to the file.

      Parameters:
      - user (dict): A dictionary containing the details of the new user (e.g., name, email, password).

      Returns:
      - dict: Success message with user details or an error message if validation or file writing fails.
      """

    name = user.get("name")
    email = user.get("email")
    password = user.get("password")

    if not name or not email or not password:
        raise HTTPException(status_code=400, detail="Name, email and password are required.")

    try:
        add_user = await read_file_for_users(users_file)
    except FileError:
        add_user = []

    for find_user in add_user:
        if find_user.get("email") == email and find_user.get("password") == password:
            raise HTTPException(status_code=409, detail="A user with this email already exists.")

    if add_user:
        max_id = max(u["id"] for u in add_user) if add_user else 0
        new_id = max_id + 1
    else:
        new_id = 1

    user["id"] = new_id
    add_user.append(user)

    try:
        await write_file_for_users(users_file, add_user)
    except FileError as e:
        raise HTTPException(status_code=500, detail=f"Failed to save user: {str(e)}")

    return {"message": f"User added: {user}"}


@app.post("/users/login")
async def login(user: dict):
    """
       Logs in a user by verifying their email and password.

       Parameters:
       - user (dict): A dictionary containing the login credentials (email and password).

       Returns:
       - dict: A welcome message if login is successful, or an error message if login fails.
       """

    email = user.get("email")
    password = user.get("password")

    if not email or not password:
        raise HTTPException(status_code=400, detail="Email and password are required.")

    try:
        users = await read_file_for_users(users_file)
    except FileError as e:
        raise HTTPException(status_code=404, detail=str(e))

    for find_user in users:
        if find_user.get("email") == email and find_user.get("password") == password:
            return {"message": f"Welcome, {find_user['name']}!"}

    raise HTTPException(status_code=401, detail="Invalid email or password.")


@app.put("/users/{user_id}")
@validator_for_user
async def update_user(user_id: int, user: dict = Body(...)):
    """
        Updates the details of an existing user.

        Parameters:
        - user_id (int): The unique ID of the user to be updated.
        - user (dict): A dictionary containing the updated user details.

        Returns:
        - dict: Success message with updated user details or an error message if the user is not found or an error occurs.
        """

    try:
        users = await read_file_for_users(users_file)
        for existing_user in users:
            if existing_user.get("id") == user_id:
                existing_user.update(user)
                await write_file_for_users(users_file, users)
                return {"message": "User updated successfully", "user": existing_user}
        raise NotFoundError(f"User with id {user_id} not found.")
    except FileError as e:
        return {"error": str(e)}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    """
       Deletes a user by their unique ID.

       Parameters:
       - user_id (int): The unique ID of the user to be deleted.

       Returns:
       - dict: Success message indicating user was deleted or an error message if the user is not found.
       """

    try:
        users = await read_file_for_users(users_file)
    except FileError as e:
        return {"error": str(e)}

    for user in users:
        if user.get("id") == user_id:
            users.remove(user)
            await write_file_for_users(users_file, users)
            return {"message": f"User with id {user_id} deleted successfully."}

    raise NotFoundError(f"User with id {user_id} not found.")


@app.get("/tasks")
async def get_tasks():
    """
       Retrieves all tasks from the JSON file.

       Purpose:
       - Fetches and returns a list of all tasks stored in the JSON file.

       Returns:
       - list: A list of all task dictionaries, or an empty list if no tasks are found.
       - dict: An error message if a file error occurs during the read operation.

       Raises:
       - FileError: If the file containing tasks cannot be read or does not exist.
       """

    try:
        all_tasks = await read_file_for_tasks(tasks_file)
        if len(all_tasks) == 0:
            return []
        else:
            return all_tasks
    except FileError as e:
        return {"error": str(e)}


@app.get("/tasks/{task_id}")
async def get_task_by_id(task_id: int):
    """
       Retrieves a task by its unique ID.

       Purpose:
       - Searches for a task in the JSON file based on the provided `task_id` and returns the task's details if found.

       Parameters:
       - task_id (int): The unique ID of the task to retrieve.

       Returns:
       - dict: A success message with the task details if found.
       - dict: An error message if the task is not found or a file error occurs.

       Raises:
       - NotFoundError: If no task is found with the specified `task_id`.
       - FileError: If the file containing tasks cannot be read or does not exist.
       """

    try:
        tasks = await read_file_for_tasks(tasks_file)
        for task in tasks:
            if task_id == task.get("user_id"):
                return {f"message: Found {task}"}
                break
        raise NotFoundError(f"Task with id {task_id} not found.")
    except FileError as e:
        return {"error": str(e)}


@app.post("/tasks")
@validator_for_task
async def create_task(new_task: dict):
    """
       Creates a new task and associates it with a user.

       Purpose:
       - Validates the user ID associated with the task, then adds the new task to the JSON file if the user exists.

       Parameters:
       - new_task (dict): A dictionary containing the task details (e.g., `user_id`, `title`, `description`).

       Returns:
       - dict: A success message with the newly created task details.
       - dict: An error message if the user ID is not found or if a file error occurs during read/write operations.

       Raises:
       - FileError: If the file containing tasks or users cannot be read.
       - HTTPException: If the task cannot be saved due to file write issues.
       """

    try:
        add_task = await read_file_for_tasks(tasks_file)
    except FileError:
        add_task = []

    try:
        search_user = await read_file_for_users(users_file)
    except FileError as e:
        return {"error": str(e)}

    user_exists = False
    for user in search_user:
        if new_task.get("user_id") == user["id"]:
            user_exists = True
            new_task["id"] = user["id"]
            break

    if not user_exists:
        return {f"No user found with id {new_task['user_id']}"}

    tasks = [task for task in add_task if task["user_id"] != new_task["user_id"]]
    tasks.append(new_task)

    try:
        await write_file_for_tasks(tasks_file, tasks)
    except FileError as e:
        raise HTTPException(status_code=500, detail=f"Failed to save task: {str(e)}")

    return {"message": f"Task added: {new_task}"}


@app.put("/tasks/{task_id}")
@validator_for_task
async def change_task(task_id: int, new_task: dict = Body(...)):
    """
       Updates an existing task based on its ID.

       Purpose:
       - Modifies the details of a task with the specified `task_id` using the provided `change_info`.

       Parameters:
       - task_id (int): The unique ID of the task to be updated.
       - change_info (dict): A dictionary containing the updated task details.

       Returns:
       - dict: A success message with the updated task details if the update is successful.
       - dict: An error message if the task is not found or a file error occurs.

       Raises:
       - NotFoundError: If no task is found with the specified `task_id`.
       - FileError: If the file containing tasks cannot be read or written to.
       """

    try:
        tasks = await read_file_for_tasks(tasks_file)
        for task in tasks:
            if task.get("user_id") == task_id:
                task.update(new_task)
                await write_file_for_tasks(tasks_file, tasks)
                return {"message": "Task updated successfully", "task": task}
        raise NotFoundError(f"Task with id {task_id} not found.")
    except FileError as e:
        return {"error": str(e)}


@app.delete("/tasks{del_id}")
async def delete_by_id(del_id):
    """
      Deletes a task based on its ID.

      Purpose:
      - Removes a task with the specified `del_id` from the JSON file.

      Parameters:
      - del_id (int): The unique ID of the task to be deleted.

      Returns:
      - dict: A success message if the task is deleted successfully.
      - dict: An error message if the task is not found or a file error occurs.

      Raises:
      - NotFoundError: If no task is found with the specified `del_id`.
      - FileError: If the file containing tasks cannot be read or written to.
      """

    try:
        tasks = await read_file_for_tasks(tasks_file)
    except FileError as e:
        return {"error": str(e)}

    for task in tasks:
        if task.get("user_id") == del_id:
            tasks.remove(task)
            await write_file_for_tasks(tasks_file, tasks)
            return {"message": f"Task with id {del_id} deleted successfully"}
    raise NotFoundError(f"Task with id {del_id} not found.")


if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)

