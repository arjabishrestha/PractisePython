#filter function
nums = [3, 2, 5, 2, 20, 27, 19]
#filter numbers greater than 10
filtered_nums = list(filter(lambda x : x > 10, nums))
print(filtered_nums)
#filter even numbers
even_nums = list(filter(lambda x : x % 2 == 0, nums))
print(even_nums)
#filter numbers greater than average
s = 0
for num in nums:
    s = s + num
average = s / len(nums)
greater_than_avg = list(filter(lambda x : x > average, nums))
print(greater_than_avg)

#lambda with map()
squares = list(map(lambda x : x ** 2, nums))
print(squares)

#lambda with sorted()
sorted_nums = sorted(nums, key = lambda x: x * -1) #on the basis of result of the number when multiplied by 1
print(sorted_nums)

pairs = [(1,1), (2,4) , (8,1), (2,5), (4,7), (3,3)]
sorted_pairs = sorted(pairs, key = lambda x: x[1])
print(sorted_pairs)

#lamnda function to compute f(x) = 2x + 5
result = lambda x : 2 * x + 5
print(result(3))
