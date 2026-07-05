#write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers

nums = [1,2,3,4,5,6]

even_nums = list(filter(lambda x: x % 2 == 0,nums))

print(len(even_nums))