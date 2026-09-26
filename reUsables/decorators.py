def prettyPrint(func):
    def wrapper(*args, **kwargs):
        # Call the original function and wrap its output in <b> tags
        result = func(*args, **kwargs)
        return f"==============\n<b>{result}</b>==============\n"

    return wrapper
