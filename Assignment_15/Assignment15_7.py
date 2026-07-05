# Write a lambda function using reduce() which accepts a list of strings and returns a list of strings having length greater than 5.

names = ["PPA", "Python", "Marvellous", "LB"]

Data = list(filter(lambda x: len(x) > 5, names))

print(Data)