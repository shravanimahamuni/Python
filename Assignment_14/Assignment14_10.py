# write a lambda function which accepts three numbers and returns largest number.

largest = lambda a, b, c: a if a > b and a > c else (b if b > c else c)

print(largest(10,20,30))