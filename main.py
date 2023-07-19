from nimaiplayer import NimAiPlayer
from trainai import train_same_ai
from playgame import playgame
from nimgame import NimGame

def train(n):
    """
    Train an AI by playing `n` games against itself.
    """

    player = NimAiPlayer()

    # Play n games
    for i in range(n):
        print(f"Playing training game {i + 1}")
        game = NimGame()

        # Keep track of last move made by either player
        last = {
            1: {"state": None, "action": None},
            2: {"state": None, "action": None}
        }

        # Game loop
        while True:

            # Keep track of current state and action
            state = game.board.copy()
            action = player.choose_action(game.board)

            # Keep track of last state and action
            last[game.player]["state"] = state
            last[game.player]["action"] = action

            # Make move
            game.make_move(action)
            new_state = game.board.copy()

            # When game is over, update Q values with rewards
            if game.winner is not None:
                print("For winner ", state, action, new_state)
                print("For loser ", last[game.player]["state"], last[game.player]["action"], new_state)
            
                player.update(state, action, new_state, -1)
                player.update(
                    last[game.player]["state"],
                    last[game.player]["action"],
                    new_state,
                    1
                )
                break

            # If game is continuing, no rewards yet
            elif last[game.player]["state"] is not None:
                player.update(
                    last[game.player]["state"],
                    last[game.player]["action"],
                    new_state,
                    0
                )

    print("Done training")

    # Return the trained AI
    return player

NUM_TRAINING_GAMES = 20000
def main():
    #Create AI player
    ai_player = NimAiPlayer()

    # #Train it on NUM_TRAINING_GAMES training games
    train_same_ai(ai_player, NUM_TRAINING_GAMES)

    # ai_player = train(NUM_TRAINING_GAMES)

    #Play a game
    playgame(ai_player)

if __name__ == '__main__':
    main()