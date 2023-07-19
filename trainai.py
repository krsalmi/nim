from nimaiplayer import NimAiPlayer
from nimgame import NimGame

#Training game will keep track of last move and update its Q values
#with rewards once game is over. If player wins, the move that 
#resulted in victory gets reward 1 and if it loses, reward is -1.
#If move results in no one winning the game, reward is 0
def training_game(ai_player):
    #Create new game
    nimgame = NimGame()

    #Dict to keep track of last move by both players
    last_move = {1: {"board": None, "move": None},
                 2: {"board": None, "move": None}
                }
    #While there is no winner, check current board and make AI player choose a move
    #which will be saved in 'last_move' dictionary
    while True:
        old_board = nimgame.board.copy()
        chosen_move = ai_player.choose_action(old_board)
        last_move[nimgame.player]["board"] = old_board
        last_move[nimgame.player]["move"] = chosen_move
        #make move and save resulting new board
        nimgame.make_move(chosen_move)
        new_board = nimgame.board.copy()
        
        # When winner is determined, update rewards so that move that resulted
        # in victory is rewarded 1 and the one that resulted in loss -1
        if nimgame.winner is not None:
            ai_player.update(last_move[nimgame.player]["board"],
                last_move[nimgame.player]["move"], new_board, 1)
            ai_player.update(old_board, chosen_move, new_board, -1)
            break

        # other moves given 0
        elif last_move[nimgame.player]["board"] is not None:
            ai_player.update(last_move[nimgame.player]["board"], 
                last_move[nimgame.player]["move"], new_board, 0)

    return ai_player

#Perform 'n' training games on same ai player
def train_same_ai(ai_player, n):
    for i in range(n):
        print("Training game number ", i + 1)
        ai_player = training_game(ai_player)
    
    return ai_player


