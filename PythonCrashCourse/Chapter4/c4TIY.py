# 4-3 Counting to Twenty:
for value in range(1, 21):
	print(value)

# 4-4/5 One Million:
million = []
for value in range(1, 1000001):
	million.append(value)
print(min(million))
print(max(million))
print(sum(million))

# 4-6 Odd Numbers:
for numbers in range(1, 21, 2):
	print(numbers)

# 4-7 Threes:
threes = []
for value in range(3, 31):
	value *= 3
	threes.append(value)
print(threes)

# 4-8 Cubes:
for value in range(1, 11):
	value **= 3
	print(value)

# 4-9 Cube Comprehension
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

# 4-10 Slices (see squares.py)

# 4-11 My Pizzas, Your Pizzas
favorite_pizzas = ['pepperoni', 'combo', 'barbeque chicken']
friends_pizzas = favorite_pizzas[:]

favorite_pizzas.append('chicken and bacon')
friends_pizzas.append('vegetarian')
count = 0
print('My favorite pizzas are:')
for pizza in favorite_pizzas:
	count += 1
	print(f'{count}.{pizza.title()}')
count = 0
print('My friends favorite pizzas are:')
for pizza in friends_pizzas:
	count += 1
	print(f'{count}. {pizza.title()}')

# 4-12 More Loops: (see foods.py)

# 4-13 Buffet:
buffet_food_items = ('steak', 'rice', 'mashed potatoes', 'mac & cheese', 'green beans')
print('\nOriginal Menu:')
for item in buffet_food_items:
	print(item.title())

buffet_food_items = ('meatloaf', 'steak', 'rice', 'mashed potatoes', 'carrots')
print('\nModified Menu:')
for item in buffet_food_items:
	print(item.title())