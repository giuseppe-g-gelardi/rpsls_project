from players import Players
import random
# TODO develop RNG for opponent moves


class Opponent(Players):
    def __init__(self, name, player_moves):
        super().__init__(name)
        self.name = name
        self.player_moves = player_moves
        print("in opponent class")


Opponent.name = "AI"
Opponent(Opponent.name, Opponent.player_moves)
print(Opponent.name)
print(Opponent.player_moves)
opponent_move = random.randint(0, 5)
print(opponent_move)
