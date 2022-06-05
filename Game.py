from BoardManager import BoardManager
from Player import Player
def initailize():
    snakes = {2: 1, 4:1, 5:1}
    ladders = {3: 100, 6:100, 7:101}
    # players = []
    # no_snakes = int(input('Enter no of snakes'))
    # for index in range(no_snakes):
    #     frm, to = input().split(' ')
    #     snakes[frm] = to
    # no_ladders = int(input('Enter no of ladders'))
    # for index in range(no_ladders):
    #     frm, to = input().split(' ')
    #     ladders[frm] = to
    # no_players = int(input('Enter no of playyer'))
    # for index in range(no_players):
    #     name = input()
    #     player = Player(1, name)
    #     players.append(player)

    # board_manager = BoardManager(no_snakes, no_ladders, snakes, ladders, players)
    board_manager = BoardManager(1, 1, snakes, ladders, [Player(1, 'kumar'), Player(1, 'Bala')])
    board_manager.play()

initailize()

    