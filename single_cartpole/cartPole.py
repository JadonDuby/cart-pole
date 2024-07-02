import gymnasium as gym
# env = gym.make("CartPole-v1")

# class CartPoleEnv(gym.Env):

#     metadata = {"render.modes": ["human", "rgb_array"], "video.frames_per_second": 50}

#     def __init__(self):

#         return 

import gym
env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset(seed=42)
for _ in range(1000):
#    action = policy(observation)  # User-defined policy function
   action = env.action_space.sample()
   observation, reward, terminated, truncated, info = env.step(action)

   if terminated or truncated:
      observation, info = env.reset()
env.close()