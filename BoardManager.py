from Dice import Dice
from Player import Player

class BoardManager:
    END_POINT = 100
    def __init__(self, no_snakes, no_ladders, snakes_map, ladders_map, players):
        self.no_snakes = no_snakes
        self.no_ladders = no_ladders
        self.snakes_map = snakes_map
        self.ladders_map = ladders_map
        self.players = players
        self.dice = Dice(6)

    def move_player(self, player, dice_roll):
        new_pos = player.get_pos() + dice_roll
        old_pos = player.get_pos()
        if new_pos in self.snakes_map:
            new_pos = self.snakes_map[new_pos]
        if new_pos in self.ladders_map:
            new_pos = self.ladders_map[new_pos]
        player.update_pos(new_pos)
        print('Player:' + player.get_name() + ' moved from ' + str(old_pos) + ' to: ' + str(new_pos))

    def play(self):
        while True:
            for player in self.players:
                self.move_player(player, self.dice.roll_dice())
                if player.get_pos() >= self.END_POINT:
                    print('Player:' + str(player.get_name()) + ' Won!!')
                    return
    

