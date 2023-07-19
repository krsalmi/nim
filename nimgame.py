

class NimGame:
    PLAYER_1 = 1
    PLAYER_2 = 2
    INITIAL_BOARD = [1, 3, 5, 7]

    def __init__(self):
        self.player = NimGame.PLAYER_1
        self.board = NimGame.INITIAL_BOARD.copy()
        self.winner = None

    def change_player(self):
        self.player = NimGame.PLAYER_1 if self.player == NimGame.PLAYER_2 else NimGame.PLAYER_2
    
    def make_move(self, move):
        (row_i, row_value) = move
        if row_i < 0 or row_i > (len(self.board) - 1):
            raise Exception("Invalid row number")
        if row_value < 1 or row_value > self.board[row_i]:
            raise Exception("Invalid number of items to remove")

        self.board[row_i] -= row_value
        self.change_player()
        self.check_winner()


    def check_winner(self):
        if all([ v == 0 for v in self.board ]):
            self.winner = self.player
    
    def print_current_board(self):
        max_len = 7
        print("Board currently:")
        for row_i, row_value in enumerate(self.board):
            print("Pile number: ", row_i, " has ", row_value, " objects")
        for row_i, row_num in enumerate(self.board):
            row_stars = "*" * row_num + " " * (len(self.board) - row_i - 1)
            print(row_stars.rjust(max_len))
        print("")
    
    @classmethod
    def get_all_available_moves(self, board):
        all_moves = []
        for row_i, row_value in enumerate(board):
            possible_moves = [(row_i, value) for value in range(row_value + 1) if value > 0]
            all_moves += possible_moves
        return all_moves