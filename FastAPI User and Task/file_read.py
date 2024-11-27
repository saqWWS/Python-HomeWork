from error import FileError
import aiofiles
import json

users_file = "users.json"
tasks_file = "tasks.json"


async def read_file_for_users(file_path):
    """
        Reads content from a JSON file asynchronously.

        Parameters:
        - file_path (str): Path to the file to be read.

        Returns:
        - dict or list: Parsed content from the JSON file.

        Raises:
        - FileError: If the file cannot be found or if the file contains invalid JSON.
        """
    try:
        async with aiofiles.open(file_path, mode="r") as file:
            content = await file.read()
            return json.loads(content)
    except FileNotFoundError:
        raise FileError("Requested resource not found.")
    except json.JSONDecodeError:
        raise FileError("Invalid JSON format in file.")


async def read_file_for_tasks(file_path):
    """
        Reads content from a JSON file asynchronously.

        Parameters:
        - file_path (str): Path to the file to be read.

        Returns:
        - dict or list: Parsed content from the JSON file.

        Raises:
        - FileError: If the file cannot be found or if the file contains invalid JSON.
        """
    try:
        async with aiofiles.open(file_path, mode="r") as file:
            content = await file.read()
            return json.loads(content)
    except FileNotFoundError:
        raise FileError("Requested resource not found.")
    except json.JSONDecodeError:
        raise FileError("Invalid JSON format in file.")


async def write_file_for_users(file_path, data):
    """
        Writes data to a JSON file asynchronously.

        Parameters:
        - file_path (str): Path to the file where data should be written.
        - data (dict or list): Data to be written to the file.

        Returns:
        - None

        Raises:
        - FileError: If the file cannot be written to.
        """
    try:
        async with aiofiles.open(file_path, mode="w") as file:
            await file.write(json.dumps(data, indent=2))
    except Exception as e:
        raise FileError(f"Failed to write file: {str(e)}")


async def write_file_for_tasks(file_path, data):
    """
        Writes data to a JSON file asynchronously.

        Parameters:
        - file_path (str): Path to the file where data should be written.
        - data (dict or list): Data to be written to the file.

        Returns:
        - None

        Raises:
        - FileError: If the file cannot be written to.
        """
    try:
        async with aiofiles.open(file_path, mode="w") as file:
            await file.write(json.dumps(data, indent=2))
    except Exception as e:
        raise FileError(f"Failed to write file: {str(e)}")

