import random
# Checking for the magic number, which may accidentaly become a number guessing
# generator

guess_max = 100
answer = random.randint(0, guess_max)

print(answer)

user_guess = input(f'Guess a number between 1 and {guess_max}:\n')

if int(user_guess) != answer:
    print('Better luck next time!')
else:
    print('Well done! You have beat the game!')

