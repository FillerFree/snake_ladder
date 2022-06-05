from BoardManager import BoardManager
from Player import Player
def initailize():
    snakes = {}
    ladders = {}
    players = []
    no_snakes = int(input('Enter no of snakes'))
    for index in range(no_snakes):
        frm, to = input().split(' ')
        snakes[frm] = to
    no_ladders = int(input('Enter no of ladders'))
    for index in range(no_ladders):
        frm, to = input().split(' ')
        ladders[frm] = to
    no_players = int(input('Enter no of playyer'))
    for index in range(no_players):
        name = input()
        player = Player(1, name)
        players.append(player)

    board_manager = BoardManager(no_snakes, no_ladders, snakes, ladders, players)
    board_manager = BoardManager(no_snakes, no_ladders, snakes, ladders, players)
    board_manager.play()

initailize()
