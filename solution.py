import pandas as pd
import numpy as np

from scipy.stats import gamma


chat_id = 411809593 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    const = 2 / (83 ** 2)
    mean_a = const * (gamma.ppf((1 - p) / 2, x.size) / x.size + x.mean() - 0.5)
    mean_b = const * (gamma.ppf((1 + p) / 2, x.size) / x.size + x.mean() - 0.5) 
    return mean_a, mean_b
