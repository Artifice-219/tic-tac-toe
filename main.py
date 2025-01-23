from classes import *

board = Board()


board.put(0,1, 'x')
# board.get_board()
board.put(1,1, 'x')
# board.get_board()
board.put(2, 1, 'x')
# board.get_board()
board.get_board()
board.is_solved('x')


def game_loop():
    print('Game is running')


# simulate continous game running
for i in range(10):
    game_loop()