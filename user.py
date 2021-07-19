from players import Players


class User(Players):
    def __init__(self, name, player_moves):
        super().__init__(name)
        self.name = name
        self.player_moves = player_moves
        print("in user class")

    def choice(self):
        self.choice = input('Please choose: rock, paper, scissors, lizard, or Spock ')
        if self.choice in self.player_moves:
            print(self.choice)
        else:
            while self.choice not in self.player_moves:
                print('sorry invalid choice! Please select rock, scissors, paper, lizard or spock')
                self.choice = input('Please choose: rock, paper, scissors, lizard, or Spock ')
                # if self.choice in self.player_moves:
                #     return self.choice
        print(f'your choice was {self.choice} ')




# test = User('Player 1', User.player_moves)

# test = test.choice()

# print(test)
