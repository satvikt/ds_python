def decorator(timeout):
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                pass
        return wrapper
    return outer_wrapper

def outer(x):
