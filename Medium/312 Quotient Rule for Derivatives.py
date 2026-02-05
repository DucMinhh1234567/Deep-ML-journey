# Implement a function that computes the derivative of 
# the quotient of two polynomial functions at a given point 
# using the quotient rule.

# Given two polynomials g(x) and h(x) represented by their coefficients, 
# compute the derivative of f(x) = g(x)/h(x) at a specific point x.

# Polynomial coefficients are given in descending order of powers. 
# For example, [1, 2, 3] represents x^2 + 2x + 3.

# Your function should:

# Accept coefficients of the numerator polynomial g(x)
# Accept coefficients of the denominator polynomial h(x)
# Accept a point x at which to evaluate the derivative
# Return the value of f'(x) at the given point
# Assume the denominator h(x) is non-zero at the evaluation point.

# Example:
# Input:
# g_coeffs = [1, 0, 1], h_coeffs = [1, 2], x = 2.0
# Output:
# 0.6875
# Reasoning:
# g(x) = x^2 + 1, h(x) = x + 2. At x = 2: g(2) = 5, h(2) = 4, g'(2) = 4, h'(2) = 1. 
# Using the quotient rule: f'(2) = (4 * 4 - 5 * 1) / 16 = 11/16 = 0.6875


import numpy as np

def poly_value(coeffs: list, x: float) -> float:
    result = 0
    n = len(coeffs)
    for i in range (0, n):
        power = n - 1 - i
        result += coeffs[i] * (x ** power)
    return result

def poly_derivative_value(coeffs: list, x: float) -> float:
    result = 0
    n = len(coeffs)
    for i in range (0, n):
        power = n - 1 - i
        if power > 0:
            result += coeffs[i] * (power) * (x ** (power - 1))
    return result

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    gx = poly_value(g_coeffs, x)
    hx = poly_value(h_coeffs, x)
    deri_gx = poly_derivative_value(g_coeffs, x)
    deri_hx = poly_derivative_value(h_coeffs, x)

    result = ((hx * deri_gx) - (gx * deri_hx)) / (hx * hx)

    return result


# Cách dùng thư viện thay vì viết chay
# def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
#     # g(x), h(x) -> Hàm tính đa thức trục tiếp
#     gx = np.polyval(g_coeffs, x)
#     hx = np.polyval(h_coeffs, x)

#     # g'(x), h'(x) -> Hàm tính đạo hàm của đa thức
#     g_der = np.polyder(g_coeffs)
#     h_der = np.polyder(h_coeffs)

#     gpx = np.polyval(g_der, x)
#     hpx = np.polyval(h_der, x)

#     # Quotient rule
#     return (gpx * hx - gx * hpx) / (hx ** 2)