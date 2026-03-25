def greet(func):
    def wrap():
        print("hello")
        func()
    return wrap()
@greet
def morning():
    print("arjabi maam")
# Steps:
# morning = greet(morning)
# goes to return wrap() --> this calls wrap function bc of bracket
# prints hello and then calls func()
# prints arjabi maam


def greet(func):
    def wrap():
        print("hello")
        func()
    return wrap
@greet
def morning():
    print("arjabi maam")
morning()

#steps:
# @greet --> morning = greet(morning)
# calls greet function skips the definition of wrap and returns wrap
# morning points to wrap
# if morning() not called wrap() is never called
# morning() = wrap() (calls wrap)
# from wrap it prints hello and calls func() i.e morning() so prints arjabi maam

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__} with args: {args}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_decorator
def add_numbers(a, b):
    return a + b

print(add_numbers(5, 3))

import time

# --- The Decorator ---
def timing_decorator(func):
    def wrapper(*args, **kwargs):  # 1. Accept any arguments
        start = time.time()
        result = func(*args, **kwargs)  # 2. Run original function
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
          # 3. Return the result!
    return wrapper

# --- The Function ---
@timing_decorator
def train_model(epochs):
    time.sleep(1)  # Simulate work
    print(f"Trained for {epochs} epochs")

# --- Usage ---
train_model(10)
