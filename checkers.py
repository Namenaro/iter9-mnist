import numpy as np

def check_dispersion(sensory_array):
    if sensory_array is None:
        return None
    return np.var(sensory_array)

def check_mean(sensory_array):
    if sensory_array is None:
        return None
    return np.mean(sensory_array)

def check_perepad(sensory_array):
    if sensory_array is None:
        return None
    min = np.min(sensory_array)
    max = np.max(sensory_array)
    span = abs(max - min)
    return span

