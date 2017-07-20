# the 'yield' keyword is what makes it a generator
# Generators are better for performance because it doesn't hold
# everything in memory

# generator function
import random


def square_numbers(nums):
     for i in nums:
          yield(i * i)

my_nums = square_numbers([1, 2, 3, 4, 5])
# one way to list results
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
...
# a better way
for num in my_nums:
     print(num)

# Generator using a comprehension
my_nums = (x * x for x in [1, 2, 3, 4, 5])

# creating a list from generator values -- loses the advantages
# of having a generator function
print(list(my_nums))

# generator function


names = ['Bob', 'Jim', 'Lex', 'Alice', 'Jane', 'Liz']
majors = ['CS', 'EE', 'ME', 'Arch', 'Hist', 'English', 'Art']


def people_generator(num_people):
     for i in range(num_people):
          person = {
              'id': i,
              'name': random.choice(names),
              'major': random.choice(majors)
          }
          yield person

people = people_generator(1000)

# print(list(people))


# print(next(people))
