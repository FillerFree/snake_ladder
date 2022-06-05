import random
class Dice():
    def __init__(self, size):
        self.size = size
    def roll_dice(self):
        return random.randint(1, self.size)