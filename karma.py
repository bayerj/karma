# -*- coding: utf-8 -*-


import random

import numpy as np


class Agent(object):

    def __init__(self, n_state, n_action):
        self.n_state = n_state
        self.n_action = n_action

    def action(self, state, reward=None):
        pass

    def reset(self):
        pass


class Environment(object):

    def __init__(self, n_state, n_action):
        self.n_state = n_state
        self.n_action = n_action

    def enter(self):
        pass

    def transit(self, action):
        pass


class ContextBanditEnvironment(Environment):

    def enter(self):
        self.last_idx = random.choice(range(self.X.shape[0]))
        return self.X[self.last_idx]

    def transit(self, action):
        # Reward for last state.
        edible = self.Z[self.last_idx]
        eat = action.argmax() == 0
        if eat and edible:
            reward, regret = 5, 0
        elif eat and not edible:
            reward = 0 if np.random.randint(0, 2) == 0 else -35
            regret = -reward
        elif not eat and edible:
            reward, regret = 0, 5
        elif not eat and not edible:
            reward, regret = 0, 0

        new_state = self.enter()
        return new_state, reward, regret


def rollout(env, agent, n_timesteps):
    agent.reset()
    state_m1 = env.enter()
    reward_m1 = 0
    for _ in range(n_timesteps):
        action = agent.action(state_m1, reward_m1)
        state, reward, regret = env.transit(action)
        yield state_m1, action, reward, state, regret
        state_m1 = state
        reward_m1 = reward
