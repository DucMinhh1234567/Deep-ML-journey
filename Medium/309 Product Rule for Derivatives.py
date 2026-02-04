# Implement a function that computes the derivative of 
# the product of two polynomial functions using the product rule from calculus.

# Polynomials are represented as coefficient lists 
# where the index corresponds to the power of x. 
# For example, [3, 2, 1] represents 3 + 2x + x^2.

# Given two polynomials f(x) and g(x), your function should return 
# the coefficients of the derivative of their product (f*g)'.

# The returned coefficients should be rounded to 4 decimal places. 
# Trailing zero coefficients should be removed from the result, 
# but if the result is the zero polynomial, return [0.0].

# Example:
# Input:
# f_coeffs = [1, 2], g_coeffs = [3, 4]
# Output:
# [10.0, 16.0]
# Reasoning:
# f(x) = 1 + 2x and g(x) = 3 + 4x. First compute f'(x) = 2 and g'(x) = 4. 
# Then f*g = (1+2x)(3+4x) = 3 + 10x + 8x^2. 
# The derivative is 10 + 16x, giving coefficients [10.0, 16.0].

import numpy as np

# Tổng độ dài 2 list - 2 + 1 -> Để list có độ dài chuẩn
# def add_poly(a: list, b: list) -> list:
#     L = max(len(a), len(b))
#     res = []

#     for i in range(L):
#         ai = a[i] if i < len(a) else 0.0
#         bi = b[i] if i < len(b) else 0.0
#         res.append(ai + bi)

#     return res

def derivative(f_coeffs: list) -> list:
    if len(f_coeffs) <= 1: return [0.0]

    a_coeffs = [] 
    for i in range (1, len(f_coeffs)):
        a_coeffs.append(float(f_coeffs[i] * i))

    return a_coeffs if any(a_coeffs) else [0.0]

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.

    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i

    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places
    """
    result = []
    new_f = derivative(f_coeffs)
    new_g = derivative(g_coeffs)

    term1 = np.convolve(new_f, g_coeffs).tolist()
    term2 = np.convolve(new_g, f_coeffs).tolist()

    L = max(len(term1), len(term2))
    for i in range(L):
        t1 = term1[i] if i < len(term1) else 0.0
        t2 = term2[i] if i < len(term2) else 0.0
        result.append(float(t1 + t2))

    result = [float(round(x, 4)) for x in result]

    while len(result) > 1 and abs(result[-1]) < 1e-9:
        result.pop()
    
    return result