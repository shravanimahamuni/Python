# Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

nums = [10,15,18,30,45,50]

Data = list(filter(lambda x : x % 3 == 0 and x % 5 == 0,nums))

print(Data)