#Create a Logging Decorator that prints information before running a function.
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with args {args} ")
        result = func(*args, **kwargs)
        return result
    return wrapper
@log_decorator
def add_numbers(x, y):
    s = x + y
    return s
sum_num = add_numbers(2, 3)
print(f"The sum of numbers is {sum_num}")
