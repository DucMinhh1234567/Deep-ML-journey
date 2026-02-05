# Implement a function that calculates the magnitude 
# and direction of a gradient vector. Given a gradient vector 
# (which could represent the gradient of a loss function 
# with respect to parameters), compute:

# Magnitude: The L2 norm of the gradient vector, 
# indicating how steep the function is at that point
# Direction: The unit vector pointing in the direction of steepest ascent
# Descent Direction: The unit vector pointing 
# in the direction of steepest descent (used in gradient descent optimization)
# The function should handle the edge case where the gradient 
# is a zero vector (indicating a critical point). In this case, 
# both direction vectors should be zero vectors.

# Return a dictionary containing 
# 'magnitude' (float), 'direction' (list), and 'descent_direction' (list).

# Example:
# Input:
# gradient = [3.0, 4.0]
# Output:
# {'magnitude': 5.0, 'direction': [0.6, 0.8], 'descent_direction': [-0.6, -0.8]}
# Reasoning:
# The gradient vector is [3, 4]. The magnitude is sqrt(3^2 + 4^2) = sqrt(25) = 5.0. 
# The direction (unit vector) is [3/5, 4/5] = [0.6, 0.8], 
# pointing in the direction of steepest ascent. 
# The descent direction is the negation: [-0.6, -0.8], 
# which is the direction used in gradient descent optimization.

import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    total = 0
    n = len(gradient)
    for i in range (n):
        total += gradient[i] * gradient[i]

    magnitude = total ** 0.5
    if magnitude < 1e-12: # Trong ML nên làm như vậy
        direction = [0.0] * len(gradient)
        descent_direction = [0.0] * len(gradient)
    else:
        direction = []
        for j in range (n):
            direction.append(gradient[j] / magnitude)

        descent_direction = []
        for k in range (n):
            descent_direction.append(-direction[k])

    return {
        "magnitude": magnitude,
        "direction": direction,
        "descent_direction": descent_direction
        }

# import numpy as np

# def gradient_direction_magnitude(gradient) -> dict:
#     gradient = np.array(gradient, dtype=float) -> Chuyển dạng chuẩn để thư viện xử lý

#     magnitude = np.linalg.norm(gradient) -> tính magnitude nhanh

#     if magnitude < 1e-12:  # tránh chia cho 0
#         direction = np.zeros_like(gradient)
#         descent_direction = np.zeros_like(gradient)
#     else:
#         direction = gradient / magnitude -> vectorized operation
#         descent_direction = -direction -> Đổi dấu vector

    # return {
    #     "magnitude": magnitude,
    #     "direction": direction.tolist(),
    #     "descent_direction": descent_direction.tolist()
    # }