from functools import wraps


def singleton(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        if not hasattr(func, '__singleton'):
            func.__singleton = func(*args, **kwargs)
        return func.__singleton
    return wrapped
