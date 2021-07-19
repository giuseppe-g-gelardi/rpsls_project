from player import Player


class Human(Player):
    def __init__(self, player1, gestures):
        self.player1 = player1
        self.gestures = gestures
        print('this works')

    def player_choice(self):
        
        self.choice = input('Please choose: rock, paper, scissors, lizard, or Spock ').lower()
        if self.choice in getstures:
            print(self.choice)
        else:
            while self.choice not in getstures:
                print('sorry invalid choice! Please select rock, scissors, paper, lizzard or spock')
                self.choice = input('Please choose: rock, paper, scissors, lizard, or Spock ').lower()

test = Human('human')

test.player_choice()