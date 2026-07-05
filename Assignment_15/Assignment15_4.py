# Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all element.

from functools import reduce 

nums = [1,2,3,4]

Sum = reduce(lambda x,y: x + y, nums)

print(Sum)