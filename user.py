from players import Players


class User(Players):
    def __init__(self, name, player_moves):
        super().__init__(name)
        self.name = name
        self.player_moves = player_moves
        print("in user class")


User.name = "player1"
User(User.name, User.player_moves)
print(User.name)
print(User.player_moves)
