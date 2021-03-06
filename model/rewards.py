import math
import numpy as np

def resolve_reward(name):
	rewards = {
		"manhattan_distance": manhattan_distance,
		"euclidean_distance": euclidean_distance,
		"binary": binary
	}
	return rewards[name]

def manhattan_distance(params):
	"""
	Manhattan distance from current position to target
	Args:
	    current (tuple): x, y coordinates of the current position
	    target (tuple): x, y coordinates of the target
	Returns:
		(float): Manhattan distance from current position to target
	"""
	current, target, solution = params
	if not solution:
		return -100
	dist = abs(target[0] - current[0]) + abs(target[1] - current[1])
	target_reached = dist == 0
	return -dist + (100 * target_reached)

def euclidean_distance(params):
	current, target, solution = params
	if not solution:
		return -100
	return -np.linalg.norm(current - target)

def binary(params):
	current, target, solution = params
	if not solution:
		return -100
	if current == target:
		return 1
	return -1
