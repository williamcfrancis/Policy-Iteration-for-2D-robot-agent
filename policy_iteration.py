import numpy as np
from numpy.random import choice
import copy
import matplotlib.pyplot as plt

class State:
    def __init__(self, up, down, left, right, stay, reward=-1, value=0):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.stay = stay
        self.reward = reward
        self.value = value

    def __str__(self):
        return str(self.value)

def plot_heatmap(value, policy):
    fig, ax = plt.subplots()
    im = ax.imshow(value, cmap='YlOrRd', interpolation='nearest')
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
    ax.set_xticks(np.arange(-.5, 10, 1))
    ax.set_yticks(np.arange(-.5, 10, 1))
    for i in range(10):
        for j in range(10):
            if policy[i][j] == 'up':
                arrow = r"$\uparrow$"
            elif policy[i][j] == 'down':
                arrow = r"$\downarrow$"
            elif policy[i][j] == 'left':
                arrow = r"$\leftarrow$"
            elif policy[i][j] == 'right':
                arrow = r"$\rightarrow$"
            elif policy[i][j] == '#':
                arrow = r"$\blacksquare$"
            text = ax.text(j, i, arrow, fontsize=16, ha="center", va="center", color="black")

    ax.set_title("Value Heatmap and Optimal Policies")
    fig.tight_layout()
    plt.savefig("policy_iter_heatmap.jpg")
    plt.show()

def plot_grid(grid):
    fig, ax = plt.subplots()
    rew = np.zeros((10,10))
    for i in range(10):
        for j in range(10):
            rew[i][j] = grid[i][j].reward
    im = ax.imshow(rew, cmap='YlOrRd', interpolation='nearest')
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
    ax.set_xticks(np.arange(-.5, 10, 1))
    ax.set_yticks(np.arange(-.5, 10, 1))
    for i in range(10):
        for j in range(10):
            text = ax.text(j, i, grid[i][j].reward, fontsize=16, ha="center", va="center", color="black")
    ax.set_title("Initial Environment")
    fig.tight_layout()
    plt.savefig("policy_iter_initial.jpg")
    plt.show()

def plot_value(grid):
    fig, ax = plt.subplots()
    value = np.zeros((10,10))
    for i in range(10):
        for j in range(10):
            value[i][j] = grid[i][j].value
    im = ax.imshow(value, cmap='YlOrRd', interpolation='nearest')
    # draw gridlines
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
    ax.set_xticks(np.arange(-.5, 10, 1))
    ax.set_yticks(np.arange(-.5, 10, 1))
    for i in range(10):
        for j in range(10):
            text = ax.text(j, i, round(value[i][j],1), fontsize=6, ha="center", va="center", color="black")

    ax.set_title("Plot of the value function")
    fig.tight_layout()
    plt.savefig("value function.jpg")
    plt.show()

def policy_iteration():

    grid = [['#','#','#','#','#','#','#','#','#','#'],
            ['#', '', '', '', '', '', '', '', '','#'],
            ['#', '', '', '', '#', '#', '', '', '','#'],
            ['#', '', '', '', '#', '', '', '', '','#'],
            ['#', '', '', '', '#', '', '', '#', '','#'],
            ['#', '', '', '', '#', '', '', '#', '','#'],
            ['#', '', '', '', '', '', '', '', '','#'],
            ['#', '', '', '#', '#', '#', '#', '', '','#'],
            ['#', '', '', '', '', '', '', '', '','#'],
            ['#','#','#','#','#','#','#','#','#','#']]
    gridcopy = copy.deepcopy(grid)
    values = np.zeros((10,10))

    for i in range(10):
        for j in range(10):
            obst = False
            north = south = east = west = (i, j)
            if i-1 > 0:
                north = (i-1, j)
                
            if i+1 < 9:
                south = (i+1, j)
                
            if j+1 < 9:
                east = (i, j+1)
                
            if j-1 > 0:
                west = (i, j-1)
            stay = (i, j)
            if grid[i][j] == '#':
                obst = True
            grid[i][j] = State(north, south, west, east, stay)
            if obst == True:
                grid[i][j].reward = -10
            
    grid[8][8].reward = 10
    gamma = 0.9
    is_policy_changed = True
    
    policy = [['right' for i in range(10)] for j in range(10)]
    actions = ['up', 'down', 'left', 'right']
    flag = 0
    iter = 0
    # Policy iteration
    while is_policy_changed:
        iter+=1
        is_policy_changed = False
        # Policy evaluation
        is_value_changed = True
        val_iter = 0
        while is_value_changed:
            is_value_changed = False
            # Run value iteration for each state
            for i in range(10):
                for j in range(10):
                    # res_policy = resulting_policy(policy[i][j]) # Calculates new policy with transition probablity
                    next_state_main = getattr(grid[i][j], policy[i][j]) # Gets the next state with the policy
                    next_state_stay = getattr(grid[i][j], 'stay')
                    if(policy[i][j] == 'up' or policy[i][j] == 'down'):
                        next_state1 = getattr(grid[i][j], 'left')
                        next_state2 = getattr(grid[i][j], 'right')
                    if(policy[i][j] == 'left' or policy[i][j] == 'right'):
                        next_state1 = getattr(grid[i][j], 'up')
                        next_state2 = getattr(grid[i][j], 'down')
 
                    v = grid[i][j].reward + gamma * (grid[next_state_main[0]][next_state_main[1]].value*0.7 
                        + grid[next_state_stay[0]][next_state_stay[1]].value*0.1 
                        + grid[next_state1[0]][next_state1[1]].value*0.1 
                        + grid[next_state2[0]][next_state2[1]].value*0.1)

                    # Compare to previous iteration
                    if v != grid[i][j].value:
                        is_value_changed = True
                        grid[i][j].value = v
        # if flag==0:
        #     plot_value(grid)
        #     flag=1

        # Once values have converged for the policy, update policy with greedy actions
        for i in range(10):
            for j in range(10):
                # Dictionary to get value associated with each action
                action_values = {a: grid[getattr(grid[i][j], a)[0]][getattr(grid[i][j], a)[1]].value for a in actions}
                best_action = max(action_values, key=action_values.get)
                # Compare to previous policy
                if best_action != policy[i][j]:
                    is_policy_changed = True
                    policy[i][j] = best_action

    for i in range(10): # Placing back the obstacles
        for j in range(10):
            if gridcopy[i][j] == '#':
                policy[i][j] = '#'
            values[i][j] += grid[i][j].value
    plot_value(grid)
    plot_heatmap(values, policy)

    return(policy)
    
if __name__ == "__main__":
    policy = policy_iteration()