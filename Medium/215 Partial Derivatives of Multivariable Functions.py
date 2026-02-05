# Implement a function to compute partial derivatives of 
# multivariable functions at a given point. 
# Partial derivatives measure the rate of change with respect to 
# one variable while holding others constant. 
# Given a function name and a point, return 
# the tuple of all partial derivatives at that point.

# Example:
# Input:
# func_name='poly2d', point=(2.0, 3.0)
# Output:
# (21.0, 16.0)
# Reasoning:
# f(x,y) = x²y + xy². ∂f/∂x = 2xy + y² = 2(2)(3) + 9 = 21. 
# ∂f/∂y = x² + 2xy = 4 + 2(2)(3) = 16. Gradient at (2,3) is (21, 16).

import numpy as np

def compute_partial_derivatives(func_name: str, point: tuple[float, ...]) -> tuple[float, ...]:
	"""
	Compute partial derivatives of multivariable functions.
	
	Args:
		func_name: Function identifier
			'poly2d': f(x,y) = x²y + xy²
			'exp_sum': f(x,y) = e^(x+y)
			'product_sin': f(x,y) = x·sin(y)
			'poly3d': f(x,y,z) = x²y + yz²
			'squared_error': f(x,y) = (x-y)²
		point: Point (x, y) or (x, y, z) at which to evaluate
	
	Returns:
		Tuple of partial derivatives (∂f/∂x, ∂f/∂y, ...) at point
	"""
import numpy as np

def compute_partial_derivatives(func_name: str, point: tuple[float, ...]) -> tuple[float, ...]:
    p = np.array(point, dtype=float)

    if func_name == "poly2d":
        x, y = p
        return (
            2 * x * y + y**2,
            x**2 + 2 * x * y
        )

    elif func_name == "exp_sum":
        x, y = p
        val = np.exp(x + y)
        return (val, val)

    elif func_name == "product_sin":
        x, y = p
        return (
            np.sin(y),
            x * np.cos(y)
        )

    elif func_name == "poly3d":
        x, y, z = p
        return (
            2 * x * y,
            x**2 + z**2,
            2 * y * z
        )

    elif func_name == "squared_error":
        x, y = p
        diff = x - y
        return (
            2 * diff,
            -2 * diff
        )

    else:
        raise ValueError(f"Unknown function name: {func_name}")