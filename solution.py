import numpy as np
from reinforcement_learning_framework import ActorCriticAgent
from noc_simulator import NOCSimulator  # Assuming NOCSimulator is the simulator for network-on-chip environment

# Initialize the simulation environment
env = NOCSimulator()

# Initialize the RL agent
agent = ActorCriticAgent(state_size=env.state_size, action_size=env.action_size)

# Training loop
total_episodes = 1000  # Define the total number of training episodes
for episode in range(total_episodes):
    state = env.reset()
    done = False
    while not done:
        action = agent.act(state)
        next_state, reward, done = env.step(action)
        agent.learn(state, action, reward, next_state, done)
        state = next_state

# Save the trained model
agent.save('optinoc_actor_critic_model.h5')
