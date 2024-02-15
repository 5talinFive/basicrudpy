a = list(range(0, 100, 2))
b = list(range(0, 10))
print(f'Lista a: {a}')
print(f'Lista b: {b}')
print(a + b)
print(b * 2)
print()
print('Ejercicios con lista bacia:')
fruits = list()
print(fruits)

fruits.append('apple')
print(fruits)
print(len(fruits))

fruits.append('banana')
print(fruits)
print(len(fruits))

fruits.append('kiwi')
print(fruits)
print(len(fruits))

some_fruit = fruits.pop()
print(some_fruit)
print(fruits)

some_fruit = fruits.pop(0)
print(some_fruit)
print(fruits)

del fruits[0]
print(fruits)

import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(0, 15))
print(random_numbers)

ordered_numbers = sorted(random_numbers)
print(ordered_numbers)

random_numbers.sort()
print(random_numbers)

print(dir(random_numbers))
    



