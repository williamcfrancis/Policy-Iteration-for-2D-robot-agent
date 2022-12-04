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

