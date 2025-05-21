def log_tool_call(func):
    import functools

    @functools.wraps(func)
    def sync_wrapper(*args, **kwargs):
        print(f"[TOOL CALL] {func.__name__} | args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"[TOOL RESULT] {func.__name__} | result: {result}")
        return result

    return sync_wrapper