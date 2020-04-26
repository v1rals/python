

def raises(FileNotFoundError):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except TypeError:
                print("Got error! ", FileNotFoundError)
        return wrapper
    return actual_decorator


@raises(FileNotFoundError)
def return_str():
    return "My shiny string" + 7

return_str() # Ошибка FileNotFoundError