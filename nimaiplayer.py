from nimgame import NimGame
import random

class NimAiPlayer:
    def __init__(self, alpha=0.5, epsilon=0.1):
        """
        Initialize AI with an empty Q-learning dictionary,
        an alpha (learning) rate, and an epsilon rate.
        """
        self.q = dict()
        self.alpha = alpha
        self.epsilon = epsilon

    def update(self, old_state, action, new_state, reward):
        """
        Update Q-learning model, given an old state, an action taken
        in that state, a new resulting state, and the reward received
        from taking that action.
        """
        old = self.get_q_value(old_state, action)
        best_future = self.best_future_reward(new_state)
        self.update_q_value(old_state, action, old, reward, best_future)

    def get_q_value(self, state, action):
        """
        Return the Q-value for the state `state` and the action `action`.
        If no Q-value exists yet in `self.q`, return 0.
        """
        if len(self.q) == 0:
            return 0
        q_key = (tuple(state), action)
        return 0 if q_key not in self.q else self.q[q_key]


    def update_q_value(self, state, action, old_q, reward, future_rewards):
        """
        Update the Q-value for the state `state` and the action `action`
        given the previous Q-value `old_q`, a current reward `reward`,
        and an estimate of future rewards `future_rewards`.
        """
        new_value_estimate = reward + future_rewards
        updated_q_value = old_q + self.alpha * (new_value_estimate - old_q)
        q_key = (tuple(state), action)
        self.q[q_key] = updated_q_value

    def best_future_reward(self, state):
        """
        Given a state `state`, consider all possible `(state, action)`
        pairs available in that state and return the maximum of all
        of their Q-values.
        """
        max_q_value = 0
        available_actions = NimGame.get_all_available_moves(state)
        #No available actions
        if len(available_actions) == 0:
            return 0
        for action in available_actions:
            max_q_value = max(self.get_q_value(state, action), max_q_value)
            
        return max_q_value

    def choose_action(self, state, epsilon=True):
        """
        Given a state `state`, return an action `(i, j)` to take.

        If `epsilon` is `False`, then return the best action
        available in the state (the one with the highest Q-value,
        using 0 for pairs that have no Q-values).

        If `epsilon` is `True`, then with probability
        `self.epsilon` choose a random available action,
        otherwise choose the best action available.

        If multiple actions have the same Q-value, any of those
        options is an acceptable return value.
        """
        available_actions = NimGame.get_all_available_moves(state)
        max_q_value = self.best_future_reward(state)
        random_action = random.choice(list(available_actions))
        #if max_q_value is 0, choose random move
        if max_q_value == 0:
            action = random_action
        else:
            #Get best possible action
            best_reward = 0
            for action in available_actions:
                new_reward = self.get_q_value(state, action)
                if new_reward > best_reward:
                    best_action = action
                    best_reward = new_reward
            
            #If epsilon is false, choose best action
            if epsilon == False:
                action = best_action
            #Else, choose either random move or best move with probability epsilon
            else:
                action = (random.choices([random_action, best_action], cum_weights=(self.epsilon, 1.0), k=1))[0]


        return action
    
            
