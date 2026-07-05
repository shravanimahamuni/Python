# Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element.

from functools import reduce 

nums = [10,20,30,40]

minimum = reduce(lambda x,y: x if x < y else y, nums)

print(minimum)