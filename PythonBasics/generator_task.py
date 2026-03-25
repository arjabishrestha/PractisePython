#create a generator that yields numbers from 1 to 10
def gen_num(n):
    for k in range (1,n+1):
        yield k
gen = gen_num(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))  #or use for loop that repeatedly cals next() on the iterator object

#multiplication generator
def multiply_by(n):
    for j in range(1,11):
        yield j*n
mul = multiply_by(5)
for v in mul:
    print(v)  #repeatedly cals next() on the iterator object

#filter generator
def get_evens(nums):
    for num in nums:
        if num % 2 == 0:
            yield num
even = get_evens([1,2,3,4,5,6,7,8])
for even_num in even:
    print(even_num)

#generator expression
num_list = [1,2,3,4,5]
square_gen = (x ** 2  for x in num_list )
print(type(square_gen))
for val in square_gen:
    print(val)

