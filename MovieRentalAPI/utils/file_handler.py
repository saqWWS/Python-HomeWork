films_file = "movie.json"
users_file = "users.json"
rentals_file = "rentals.json"


def read_file_for_users(file_path):
    try:
        with open(file_path, mode="r") as file:
            content = file.read()
            return json.loads(content)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    except Exception as e:
        return {e}


def write_file_for_users(file_path, data):
    try:
        with open(file_path, mode="w") as file:
            json.dump(data, file, indent=2)
    except json.JSONDecodeError as e:
        raise {e}
    except Exception as e:
        raise Exception(f"Failed to write file: {str(e)}")


def read_file_for_films(file_path):
    try:
        with open(file_path, mode="r") as file:
            content = file.read()
            return json.loads(content)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def write_file_for_films(file_path, data):
    try:
        with open(file_path, mode="w") as file:
            json.dump(data, file, indent=2)
    except Exception as e:
        raise (f"Failed to write file: {str(e)}")


def read_file_for_rentals(file_path):
    try:
        with open(file_path, mode="r") as file:
            content = file.read()
            return json.loads(content)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    except Exception as e:
        return {e}


def write_file_for_rentals(file_path, data):
    try:
        with open(file_path, mode="w") as file:
            json.dump(data, file, indent=2)
    except json.JSONDecodeError as e:
        raise {e}
    except Exception as e:
        raise Exception(f"Failed to write file: {str(e)}")
