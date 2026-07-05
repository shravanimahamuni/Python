# write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.

from functools import reduce 

nums = [1,2,3,4]

product = reduce(lambda x,y: x * y, nums)

print(product)