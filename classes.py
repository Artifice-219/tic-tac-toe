class Board:
    def __init__(self):
        self.board = [
            ['_','_', '_'],
            ['_','_', '_'],
            ['_','_', '_']
        ]
    # just displays the current board, this method musn't "re-draw" the board
    def get_board(self):
        rows = len(self.board)
        col = len(self.board)

        for r in range(rows):
            print(self.board[r][0], '|', self.board[r][1], '|', self.board[r][2],)

    # put() put chars in the specified coordinate
    def put(self, row, col, sym):
        # check if the sym is an alphabetic character
        if(sym.isalpha()):
            sym = sym.lower()
            # symbol validation
            if sym == 'x' or  sym == 'o':
                self.board[row][col] = sym
        else:
            print('Please choose only between X and O ')

    def make_board(self):
        # do some formatting here to print the board prettily
        rows = len(self.board)
        col = len(self.board)

        for r in range(rows):
            print(self.board[r][0], '|', self.board[r][1], '|', self.board[r][2],)
        