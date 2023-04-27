def decorator(func):
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        print(f"Val returned is {val}")
    return wrapper

@decorator
def sum_my(x, y):
    return x+y

sum_my(1,1)