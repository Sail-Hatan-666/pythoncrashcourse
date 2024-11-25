my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

my_foods.append('canoli')
friends_foods.append('ice cream')
print(f'My favorite foods are:\n{my_foods}\n\nMy friends favorite foods are:\n{friends_foods}')


for food in my_foods:
	print(food.title())

for food in friends_foods:
	print(food.title())