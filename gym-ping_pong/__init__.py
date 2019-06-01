from gym.envs.registration import register

register(
	id = 'ping_pong-v0',
	entry_point = 'gym_ping_pong.envs:ping_pongEnv',
	)