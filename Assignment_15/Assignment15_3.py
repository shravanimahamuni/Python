# Write a lambda function using filter() which accepts a list of numbers and returns a list of odd number.

nums = [1,2,3,4,5,6]

odd_nums = list(filter(lambda x:x % 2 != 0, nums))

print(odd_nums)