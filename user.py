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



# TODO impliment the following

# self.choice = input('Please choose: rock, paper, scissors, lizard, or Spock ').lower()
# if self.choice in getstures:
#     print(self.choice)
# else:
#     while self.choice not in getstures:
#         print('sorry invalid choice! Please select rock, scissors, paper, lizzard or spock')
#         self.choice = input('Please choose: rock, paper, scissors, lizard, or Spock ').lower()
#
# test = Human('human')
#
# test.player_choice()
