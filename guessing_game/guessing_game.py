# guessing game
# 3 turns to guess a number
import random

turns = 3
number_to_guess = random.randint(1, 10)


def check_answer(guess, number_to_guess):
    if guess < number_to_guess:
        response = "higher!"
    elif guess > number_to_guess:
        response = "lower!"
    else:
        response = f"congrats the number to guess ({number_to_guess}) is your guess({guess})"

    return response


while turns > 0:
    print(f"Enter guess ({number_to_guess}), {turns} turns left.")
    guess = int(input())
    message = check_answer(guess, number_to_guess)
    print(message)
    turns = turns - 1

if turns == 0 and message not in ["higher!", "lower!"]:
    print(f"this is loss, the number was {number_to_guess}")
