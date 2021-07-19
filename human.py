from players import Player

class Human(Player):
    def __init__(self, player1):
        self.player1 = player1
        print('this works')

    def player_choice(self, getstures):
        self.choice = input('Please choose: rock, paper, scissors, lizard, or Spock ').lower()
        if self.choice in getstures:
            print(self.choice)
        else:
            while self.choice not in getstures:
                print('sorry invalid choice! Please select rock, scissors, paper, lizzard or spock')
                choice = input('Please choose: rock, paper, scissors, lizard, or Spock ').lower()

