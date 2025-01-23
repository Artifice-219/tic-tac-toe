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
        # check if the cell at that location is free
        if(self.board[row][col] == '_'):
            if(sym.isalpha()):
                sym = sym.lower()
                # symbol validation
                if sym == 'x' or  sym == 'o':
                    self.board[row][col] = sym
            else:
                print('Please choose only between X and O ')
        else:
            print(f'Board at {row} - {col} is not free')

    def make_board(self):
        # do some formatting here to print the board prettily
        rows = len(self.board)
        col = len(self.board)

        for r in range(rows):
            print(self.board[r][0], '|', self.board[r][1], '|', self.board[r][2],)
    
    def horizontal_win(self, sym):
         # check for horizontal win
        count = 0
        for row in range(3):
            for col in range(3):
                # counts how many times does the symbol sym happen consecutively
                if(self.board[row][col] == sym):
                    count += 1
                # if the repetition is not repeating revert count to 0
                else:
                    count = 0
                if(count == 3):
                    return print('A Horizontal winning condition is found')

    def vertical_win(self, sym):
        # check for vertical win
        count = 0
        for row in range(3):
            for col in range(3):
                if(self.board[col][row] == sym):
                    count += 1
                # if the repetition is not repeating revert count to 0
                else:
                    count = 0
                if(count == 3):
                    return print('A Vertical winning condition is found')
    
    def diagonal_win(self, sym):
        # check for winning diagonal condition is sadly hardcoded
        count = 0
        if(self.board[0][0] and self.board[1][1] and  self.board[2][2]  == sym):
            return print('A diagonal winning condition is found')
        
        if(self.board[0][2] and self.board[1][1] and  self.board[2][0]  == sym):
            return print('A diagonal winning condition is found')
    
    # consolidate all functions that check for winning conditions
    def is_solved(self, sym):
        if(self.horizontal_win(sym) or self.vertical_win(sym) or self.diagonal_win(sym)):
            return True
        return False