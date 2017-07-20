# Some examples of Comprehensions - based on Corey Schafer video

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Below are some variations of list comprehensions

# simple list comprehension to create a list of numbers
my_list1 = [n for n in nums]
print(my_list1)

# create a list of the first 10 squares
my_list2 = [n * n for n in nums]
print(my_list2)
# another way using lambda functions
# it also only uses one line, but is less readable
my_list2b = list(map(lambda n: n * n, nums))
print(my_list2b)

# create list of even numbers from nums
my_list3 = [n for n in nums if n % 2 == 0]
print(my_list3)
# another way using lambda functions
# it also only uses one line, but is less readable
my_list3b = list(filter(lambda n: n % 2 == 0, nums))
print(my_list3b)

# create a list of letter,number pairs
my_list4 = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list4)

# Below are some examples of Dictionary Comprehensions

names = ['Bruce', 'Clark', 'Peter']
heros = ['Batman', 'Superman', 'Spiderman']
# print zip(names,heros)     # zip function creates tuples from lists
# Old fashioned way
my_dict1_old = {}
for name, hero in zip(names, heros):
    my_dict1_old[name] = hero
print(my_dict1_old)
# Comprehension way
my_dict1_new = {name: hero for name, hero in zip(names, heros)}
print(my_dict1_new)


# sets comprehension examples
nums = [1, 2, 1, 1, 3, 5, 2, 5, 2, 5, 6, 7, 8, 3, 2, 5, 1, 9, 5]
# old fashioned way
my_set1 = set()
for n in nums:
    my_set1.add(n)
# comprehension method
my_set2 = {n for n in nums}
print(my_set2)
