from players import Players


class Human(Players):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def gestures(self):
        self.choice = input('Please choose: rock, paper, scissors, lizard, or Spock ').lower()
        if self.choice in self.player_moves:
            print(self.choice)
        else:
            while self.choice not in self.player_moves:
                print('sorry invalid choice! Please select rock, scissors, paper, lizard or spock')
                self.choice = input('Please choose: rock, paper, scissors, lizard, or Spock ').lower()

        print(f'your choice was {self.choice} ')
        # return self.choice


# test = Human('Player 1')

# test1 = test.gestures()

