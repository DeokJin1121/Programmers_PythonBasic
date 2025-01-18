# list
# create
numbers = [0, 1, 2, 3, 4]
chars = ['a', 'b', 'c', 'd']
users = ['Allen', 'Chan', 'John', 'May']
students = ['Allen', 170, 'Chan', 165, 'John', 180, 'May', 150]
# print(numbers, chars, users, students, sep = '\n')

# access, update -> index(자리변환) -> 0
print(numbers[4])
print(users[-4])
users[-1] = 'Spencer'
print(users)

# delete -> index
del users[-1]
print(users)
del users[0]
print(users)

# del users
# print(users)

a = 3
del a
print(a)