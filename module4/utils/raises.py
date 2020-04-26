

def raises(FileNotFoundError):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except TypeError as ve:
                print("Got error! ",TypeError, ve)
                raise FileNotFoundError
        return wrapper
    return actual_decorator

