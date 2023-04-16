import game as g
import matplotlib.pylab as plt
import numpy as np


def plot_agent_reward(rewards):
    """ Function to plot agent's accumulated reward vs. iteration """
    plt.plot(np.cumsum(rewards))
    plt.title('Agent Cumulative Reward vs. Iteration')
    plt.ylabel('Reward')
    plt.xlabel('Episode')
    plt.show()


class GameLearning:

    def __init__(self):
        while True:
            print('\nChoose a mode:')
            mode = input('1. Agent RL vs Agent AI \n2. Agent RL vs Human \n3. Agent RL vs Agent RL\nMode nº = ')
            if mode == '1' or mode == '2' or mode == '3':
                break
        if mode == '1':
            self.game = g.Game('agentAI')
        elif mode == '2':
            self.game = g.Game('human')
        else:
            self.game = g.Game('agentRL')

    def begin_playing(self):
        self.game.play()


if __name__ == '__main__':
    gl = GameLearning()
    gl.begin_playing()
