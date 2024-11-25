# squares = []

# Initial attempt
# for value in range(1, 11):
# 	square = value ** 2
# 	squares.append(square)

# print(squares)

# Optimized attempt
# for value in range(1, 11):
# 	squares.append(value ** 2)

# print(squares)

# List Comprehension

squares = [value ** 2 for value in range(1, 11)]

print(squares)

print(f'The first three items in the list are: {squares[:3]}')
print(f'Three items from the middle of the list are: {squares[4:7]}')
print(f'The last three items in the list are: {squares[-3:]}')