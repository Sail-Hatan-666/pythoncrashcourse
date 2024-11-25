import random
# Checking for the magic number, which may accidentaly become a number guessing
# generator

answer = random.randint(0, 20)

print(answer)

user_guess = input('Guess a number between 1 and 20:\n')

if int(user_guess) == answer:
    print('Well done! You have won the game.')
else:
    print('Better luck next time!')

