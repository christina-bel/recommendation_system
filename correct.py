
import numpy as np

correct = lambda x: round(max(min(x, 5),1)) if x != 0 else 0
vectorized_correct = np.vectorize(correct)

def correct_numbers(x):
    return vectorized_correct(x)
