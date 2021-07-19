class Players:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.player_moves = ["rock", "paper", "scissors", "lizard", "spock"]


    # def choose_gesture(self):
    #     """
    #     every child class should implement this: return a String gesture choice
    #     return a String gesture
    #     """
    #     pass

        
# class Human(Players):
#     def __init__(self, name):
#         super().__init__(name)

#     def choose_gesture(self):
#         # implement with user selection
#         return super().choose_gesture()



# class AI(Players):
#     def __init__(self, name):
#         super().__init__(name)

#     def choose_gesture(self):
#         # implement with random selection
#         return super().choose_gesture()