# A normal function (Creates a full list in memory)
def square_list(n):
    result = []
    for i in range(n):
        result.append(i * i)
    return result  # Returns [0, 1, 4, 9...] all at once

# A generator function (Creates items one by one)
def square_generator(n):
    for i in range(n):
        yield i * i  # Pauses here, gives value, waits for next()

# Usage
gen = square_generator(5)
print(next(gen))  # 0
print(next(gen))  # 1
# Or use in a loop
for val in square_generator(5):
    pass # Processes one by one without storing all in memory