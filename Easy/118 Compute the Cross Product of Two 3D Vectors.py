# Implement a function to compute the cross product of two 
# 3-dimensional vectors. The cross product of two vectors results 
# in a third vector that is perpendicular to both and follows 
# the right-hand rule. This concept is fundamental in physics, 
# engineering, and 3D graphics.

# Example:
# Input:
# cross_product([1, 0, 0], [0, 1, 0])
# Output:
# [0, 0, 1]
# Reasoning:
# The cross product of two orthogonal unit vectors 
# [1, 0, 0] and [0, 1, 0] is [0, 0, 1], 
# pointing in the positive z-direction as per the right-hand rule.

import numpy as np

def cross_product(a, b):
    a = np.array(a)
    b = np.array(b)

    if a.shape != (3,) or b.shape != (3,):
        raise ValueError("Lỗi")

    return np.cross(a, b)
