import gym


env = gym.make('CartPole-v0')
env.reset()
for _ in range(100):
    env.render()
    action = env.action_space.sample()
    observation, reward, done, info  = env.step(action) # take a random action
    print observation
    print reward
    print done
