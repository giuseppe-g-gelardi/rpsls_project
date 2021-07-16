from player import Player

class Human(Player):
    def __init__(self, player1):
        self.player1 = ''
        print('this works')

    def player_choice(self):
        self.choice = input('Please choose: R for rock, P for paper, S for scissors, L for lizzard, and SP for Spock ')
        print(self.choice)