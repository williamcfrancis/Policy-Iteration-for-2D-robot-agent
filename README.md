# Policy Iteration Algorithm
Policy Iteration is a way to find the optimal policy for given states and actions

Let us assume we have a policy (𝝅 : S → A ) that assigns an action to each state. Action 𝝅(s) will be chosen each time the system is at state s.

The policy iteration algorithm can be summarized into three main steps:
1. Evaluate a given policy (eg. initialise policy arbitrarily for all states s ∊ S) by calculating value function for all states s ∊ S under the given policy.
![image](https://user-images.githubusercontent.com/38180831/205469967-74405822-ccdb-45f1-8843-114d6fbb6ed7.png)
Value function = the expected reward collected at the first step + expected discounted value at the next state

2. Improve policy : find a better action for state s ∊ S
![image](https://user-images.githubusercontent.com/38180831/205469978-26a53536-9efa-4c80-aed7-0f7cd46ce713.png)

3. Repeat step 1,2 until value function converge to optimal value function

## The 2D Robot Agent Problem

To run and evaluate the policy iteration algorithm, we assume a 2D robot agent problem.\
Consider the following Markov Decision Process. The state-space is a 10×10 grid, cells that are obstacles are marked in gray. The initial state of the robot is in blue and our desired terminal state is in green. The robot gets a reward of 10 if it reaches the desired terminal state with a discount factor of 0.9. At each non-obstacle cell, the robot can attempt to move to any of the immediate neighboring cells using one of the four controls (North, East, West and South). The robot cannot move diagonally. The move succeeds with probability 0.7 and with remainder probability 0.3 the robot can end up at some other cell as follows:\

P(moves north |control is north) = 0.7,\
P(moves west |control is north) = 0.1,\
P(moves east |control is north) = 0.1,\
P(does not move |control is north) = 0.1.\

![image](https://user-images.githubusercontent.com/38180831/205470046-f48aa714-dcd1-4945-bb87-4f40206ae433.png)

Similarly, if the robot desired to go east, it may end up in the cells to its north, south, or stay put at the original cell with total probability 0.3 and actually move to the cell east with probability 0.7. The cost pays a cost of 1 (i.e., reward is -1) for each control input it takes, regardless of the outcome. If the robot ends up at a state marked as an obstacle, it gets a reward of -10 for each time-step that it remains inside the obstacle cell. We would like to implement policy iteration to find the best trajectory for the robot to go from the blue cell to the green cell.

## Results

#### Plotting the initial environment to verify that it confirms to the picture in the question,
![image](https://user-images.githubusercontent.com/38180831/205470113-67a7f94e-b127-4ede-a1d0-ac6a57821088.png)

#### Plot of the value function after 1 iteration:
![image](https://user-images.githubusercontent.com/38180831/205470128-b53a3df2-d4b7-4a47-98cf-9f79ccb8876b.png)

#### Final plot of the value function:
![image](https://user-images.githubusercontent.com/38180831/205470140-49d34993-85db-46b2-9828-37755c229450.png)

#### Plot of the policy after 1 iteration:
![image](https://user-images.githubusercontent.com/38180831/205470153-2ac7cfb1-8693-47c7-8c10-029c51ddcdcc.png)

#### Plot of the policy after 2 iterations:
![image](https://user-images.githubusercontent.com/38180831/205470174-3b24b34f-a44e-486f-b2a1-0af19899e579.png)

#### Plot of the policy after 3 iterations
![image](https://user-images.githubusercontent.com/38180831/205470189-3f3b0270-8537-4827-a1cf-ae87266f4144.png)

#### Plot of the policy after 4 iterations
![image](https://user-images.githubusercontent.com/38180831/205470196-baa21dca-1c77-4fe6-8671-4264b15fd4c0.png)
