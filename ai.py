from players import Players
import random


class AI(Players):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
    

    def AI(self):
        self.computer = AI('Mr Robot')

    def choice(self):
        self.opponent_move = random.randint(0, 4)
        
        self.opponent_random_move = self.player_moves[self.opponent_move]

        print(f'AI picked {self.opponent_random_move}')


# test = AI('robot')

# test = test.choice()



