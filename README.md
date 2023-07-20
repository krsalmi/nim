# nim
![NimGame svg](https://github.com/krsalmi/nim/assets/57495339/b9b63ae4-558b-4970-b701-1e707578cd0e)

Nim is a two-player mathematical game of strategy where players take turns removing objects from distinct heaps or piles.
On each turn, a player must remove at least one object, and may remove any number of objects provided they all come 
from the same heap or pile. The goal is to force your opponent to have to pick up the last object; hence, the player who avoids 
making the last move wins.  
  
This project is inspired by an exercise I worked on for the [Harvard AI50 course](https://cs50.harvard.edu/ai/2020/). In this version,
there are 2 game modes: Human vs AI, and AI vs AI. The AI player is trained with reinforcement learning (Q learning). In the second mode, 
one AI player will be trained and the other one not. The program user can determine the player number of the human in Mode 1, and the player
number of the trained AI in Mode 2.

## Studying AI concepts: Q Learning
Q-learning is a reinforcement learning algorithm in artificial intelligence where an agent learns to make optimal decisions by 
interacting with an environment. The agent keeps track of the "quality" or usefulness of each action in each situation (state) 
it encounters, hence the "Q" in Q-learning. As the agent explores the environment and experiences different outcomes, it updates 
its estimates of the Q-values, essentially learning by trial and error. These Q-values guide the agent's future decisions, gradually 
helping it figure out the best actions to take in each state to achieve its goal efficiently. 
In this project, Q learning is used to help the NimAiPlayer make better moves that hopefully lead to victory. Other common use cases 
for Q-learning could include tasks such as navigating a robot through a maze, optimizing a trading strategy, or designing a 
recommendation system.

## How to run the program
After cloning the repository, run `python main.py` from inside of the folder. First, this will trigger 'NUM_TRAINING_GAMES' number of training
games to be played to train the AI player (currently set to 20 000). After training is completed, the game will start. The user is prompted to 
choose a game mode and a player number. If mode is AI vs AI, the trained AI will always be Player 1 if not explicitly set to Player 2.  
The game will progress in turns, the number of the remaining objects in each pile will be explained in text and also shown as a pattern.  
<img width="536" alt="Screenshot 2023-07-20 at 13 48 59" src="https://github.com/krsalmi/nim/assets/57495339/4381a750-129c-42dd-be46-997989472406">
