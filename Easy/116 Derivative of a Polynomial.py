# Implement a function that computes the derivative
# of a polynomial term of the form c * x^n
# at a given point x, where c is a coefficient and n is the exponent. 
# The function should return the value of the derivative, 
# accounting for the coefficient in the power rule. 
# This is useful for understanding how polynomials change at specific points 
# in machine learning optimization problems.

def poly_term_derivative(c: float, x: float, n: float) -> float:
    if n == 0: return 0.0

    coef = c * n
    exponent = n - 1

    return coef * (x ** exponent)