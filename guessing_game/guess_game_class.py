import random


class GuessingGame:

    def __init__(self, max_tries=3):
        self.secret_number = random.randint(1, 10)
        self.max_tries = max_tries
        self.tries = 0

    def play(self):
        while self.tries < self.max_tries:
            try:
                guess = int(input(f"turn number {self.tries + 1} - make your guess: "))
            except ValueError:
                print("Please enter a number")
                continue

            self.tries += 1
            if guess == self.secret_number:
                print("You win!")
                return
            if guess > self.secret_number:
                print("lower!")
            if guess < self.secret_number:
                print("higher!")
        print(f"Game over, it was {self.secret_number}")


game = GuessingGame()
game.play()
