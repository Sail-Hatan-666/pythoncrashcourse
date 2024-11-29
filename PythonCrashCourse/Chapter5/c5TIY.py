# 5-1 Conditional Tests:
car = 'honda'
print("is car == 'honda'? My prediction is True")
print(car == 'honda')

print("is car == 'subaru'? My prediction is Frue")
print(car == 'subaru')

# 5-2 Skipped"

# 5-3 Alien Colors #1 See aliens.py

# 5-4 Alien Colors #2 See aliens.py

# 5-5 Alien Colors #3 See aliens.py

# 5-6 Stages of Life:
age = 64

if age < 2:
    print('This person is a baby')
elif age >= 2 and age < 4:
    print('This person is a toddler')
elif age >= 4 and age < 13:
    print('This person is a child')
elif age >= 13 and age < 20:
    print('This person is a teenager')
elif age >= 20 and age < 65:
    print('This person is an adult')
else:
    print('This person is an elder')

# 5-7 Favorite Fruit:
favorite_fruits = ['banana', 'grapes', 'orange']

if 'banana' in favorite_fruits:
    print('Wow, you really like bananas!')
if 'grapes' in favorite_fruits:
    print('Wow, you really like grapes!')
if 'orange' in favorite_fruits:
    print('Wow, you really like oranges!')
if 'pineapple' in favorite_fruits:
    print('Wow, you really like pineapple!')
if 'grapefruit' in favorite_fruits:
    print('Wow, you really like grapefruit!')

# 5-8/5-9 Hello Admin:
users = ['ryan', 'jesseca', 'madi', 'dan', 'admin']
# users = []
if users:
    for user in users:
        if user == 'admin':
            print(f'Hello {user.title()}, would you like to see a staus report?')
        else:
            print(f'Hello {user.title()}, thank you for logging in again')
else:
    print('We need to find some users!')

# 5-10 Checking Usernames:
current_users = ['ryan', 'jesseca', 'madi', 'dan', 'dode']
new_users = ['ryan', 'jesseca', 'madison', 'daniel', 'george']

for user in new_users:
    if user in current_users:
        print('')