def make_logger(level):
    def logger(message):
        return f"[{level}]: {message}"
    return logger
    
    
info = make_logger("INFO")
error = make_logger("ERROR")
debug = make_logger('DEBUG')
warning = make_logger('WARNING')

info_message = info("This is information message.")
error_message = error("This is error message.")
debug_message = debug("This is debug message.")
warning_message = warning("This is warning message.")

print(info_message)
print(error_message)
print(debug_message)
print(warning_message)