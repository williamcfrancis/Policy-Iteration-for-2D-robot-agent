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
![image](https://user-images.githubusercontent.com/38180831/205470031-b4ff1551-99c6-4455-823e-35fdcf105777.png)
