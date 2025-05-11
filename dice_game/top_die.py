# both players roll dice and whoever reaches the highscore first wins.
import random


class Player:
    def __init__(self, player_number):
        self.id = player_number
        self.total = 0
        self.score = 0
        self.rolls = []


class DiceGame:
    def __init__(self, number_of_dice=2, number_of_players=2, score_target=20):
        self.number_of_dice = number_of_dice
        self.target_score = score_target
        self.win = False
        self.players = []
        for player_number in range(1, number_of_players+1):
            player = Player(player_number)
            self.players.append(player)

    def roll(self):
        roll = random.randint(1, 6)
        return roll

    def play(self):
        while self.win == False:
            for player in self.players:
                for roll in range(1, self.number_of_dice +1):
                    if self.win ==True:
                        break
                    roll = self.roll()
                    player.rolls.append(roll)
                    player.total += roll
                    print(f"Player {player.id} rolled: {roll}, your running total is {player.total}")


                    if player.total > self.target_score:
                        print(f"Player {player.id} wins with a score of {player.total} ")
                        self.win = True
                        break


game = DiceGame()
game.play()