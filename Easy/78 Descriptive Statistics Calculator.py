# Write a Python function to calculate various 
# descriptive statistics metrics for a given dataset. 
# The function should take a list or NumPy array 
# of numerical values and return a dictionary containing:

# mean: Average of all values
# median: Middle value when sorted
# mode: Most frequently occurring value
# variance: Population variance (divide by N)
# standard_deviation: Square root of variance
# 25th_percentile, 50th_percentile, 75th_percentile: Quartile values
# interquartile_range: Difference between 75th and 25th percentiles (IQR)

# Example:
# Input:
# [1, 2, 2, 3, 4, 4, 4, 5]
# Output:
# {'mean': 3.125, 'median': 3.5, 'mode': 4, 'variance': 1.6094, 
#  'standard_deviation': 1.2686, ...}
# Reasoning:
# Mean = (1+2+2+3+4+4+4+5)/8 = 3.125. 
# Median = average of 4th and 5th values = (3+4)/2 = 3.5. 
# Mode = 4 (appears 3 times, most frequent). 
# Variance and standard deviation measure spread around the mean. 
# Percentiles divide the sorted data into quarters.

import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    arr = np.asarray(data, dtype=float)
    
    if arr.size == 0:
        raise ValueError("Dataset cannot be empty")
    
    # mean
    mean = np.mean(arr)
    # median
    median = np.median(arr)
    #mode
    values, counts = np.unique(arr, return_counts=True)
    mode = int(values[np.argmax(counts)])
    # Population variance (chia cho N)
    variance = np.var(arr)   # mặc định ddof=0 → chia cho N
    # Standard deviation
    standard_deviation = np.std(arr)  # mặc định ddof=0
    # Percentiles
    p25 = np.percentile(arr, 25)
    p50 = np.percentile(arr, 50)
    p75 = np.percentile(arr, 75)
    # Interquartile Range (IQR)
    iqr = p75 - p25
    
    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": variance,
        "standard_deviation": standard_deviation,
        "25th_percentile": p25,
        "50th_percentile": p50,
        "75th_percentile": p75,
        "interquartile_range": iqr
    }