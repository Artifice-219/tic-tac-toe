class Board:
    def __init__(self):
        self.board = [
            ['_','_', '_'],
            ['_','_', '_'],
            ['_','_', '_']
        ]

    def make_board(self):
        # do some formatting here to print the board prettily
        rows = len(self.board)
        col = len(self.board)

        for r in range(rows):
            print(self.board[r][0], '|', self.board[r][1], '|', self.board[r][2],)
        