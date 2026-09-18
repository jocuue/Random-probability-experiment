import numpy as np

def generate_attempts(maximum, target):
    random_numbers = np.random.randint(1, 101, maximum)
    matches = random_numbers == target
    counter = np.sum(matches)
    return counter