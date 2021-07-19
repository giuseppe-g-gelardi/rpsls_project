from players import Players
import random
# TODO develop RNG for opponent moves


class Opponent(Players):
    def __init__(self, name, player_moves):
        super().__init__(name)
        self.name = name
        self.player_moves = player_moves

    def AI(self):
        self.computer = Opponent('Mr Robot')

    def choice(self):
        self.opponent_move = random.randint(0, 4)
        
        self.opponent_random_move = self.player_moves[self.opponent_move]

        print(f'AI picked {self.opponent_random_move}')


test = Opponent('Player 2', Opponent.player_moves)

test = test.choice()

print(test)



# Opponent.name = "AI"
# Opponent(Opponent.name, Opponent.player_moves)
# print(Opponent.name)
# print(Opponent.player_moves)
# opponent_move = random.randint(0, 4)
# print(opponent_move)
# opp_index = random.randint(0, 4)
# opponent_random_move = Opponent.player_moves[opp_index]
# print(opponent_random_move)
