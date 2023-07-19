from nimgame import NimGame
from nimaiplayer import NimAiPlayer
import random
import time

PERSON_VS_AI = 1
AI_VS_AI = 2
LEN_BOARD = 4

PLAYER_1 = 1
PLAYER_2 = 2

# Defines game mode from users input
def define_game_mode():
    print("This is the classic game of Nim, which can be played in the following 2 ways:")
    print("1 = person vs AI player")
    print("2 = two AI players")
    print("Enter number 1 or 2 according to the type of Nim mode you want")
    mode = input()
    while not mode.isdigit() or not 1 <= int(mode) <= 2:
        mode = input("Must be 1 or 2\n")
    return int(mode)

#Prompt user for player number. If not a valid number, decide player numbers randomly
def get_human_player_number():
    print("If you want to define which player number the human player will have, enter either 1 or 2.\nOtherwise, the Player 1 will be chosen randomly")
    human_player_number = input()
    if not human_player_number.isdigit() or (int(human_player_number) != 1 and int(human_player_number) != 2):
        human_player_number = random.randint(1, 2)
    else:
        human_player_number = int(human_player_number)
    return human_player_number

def get_trained_ai_player_number():
        print("If you want to define which player number the trained AI will have, enter either 1 or 2.\nOtherwise, the trained AI will always be Player 1")
        trained_ai_number = input()
        if not trained_ai_number.isdigit() or (int(trained_ai_number) != 1 and int(trained_ai_number) != 2):
            trained_ai_number = 1
        else:
            trained_ai_number = int(trained_ai_number)
        return trained_ai_number

def playgame(ai_player):
    #Let user choose game mode and then determine player number of human player, if one exists
    game_mode = define_game_mode()
    if game_mode == PERSON_VS_AI:
        human_player_number = get_human_player_number()

    #Create second ai players
    if game_mode == AI_VS_AI:
        ai_player_2 = NimAiPlayer()
        trained_ai_number = get_trained_ai_player_number()

    #Start a new game
    nimgame = NimGame()
    print("Started a new game!\n")

    while True:
        nimgame.print_current_board()
        cur_player = nimgame.player
        print("Player ", cur_player, "'s turn ", end="")
        #Handle human player's turn, if one exists
        if game_mode == PERSON_VS_AI and cur_player == human_player_number:
            print("(human player):")
            while True:
                pile_num = input("Enter the number of the pile you want to remove objects from: ")
                obj_num = input("Enter the number of objects you want to remove: ")
                if pile_num.isdigit() and obj_num.isdigit() and \
                    (int(pile_num), int(obj_num)) in nimgame.get_all_available_moves(nimgame.board):
                    move = (int(pile_num), int(obj_num))
                    break
                print("Invalid move, try again.")
        else:
            #Handle AI player's turn. Pause a bit before
            print("(AI player):")
            time.sleep(0.5)
            if game_mode == PERSON_VS_AI or cur_player == trained_ai_number:
                move = ai_player.choose_action(nimgame.board)
            else:
                move = ai_player_2.choose_action(nimgame.board)

        nimgame.make_move(move)
        
        #Check to see if winner exists
        winner = nimgame.winner
        if winner != None:
            print("\nGAME OVER!\n")
            print("Winner is Player number ", winner)
            if game_mode == PERSON_VS_AI:
                if winner == human_player_number:
                    print("Human won!")
                else:
                    print("AI won!")
            return
