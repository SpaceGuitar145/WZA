import numpy as np

def poly_divide(dividend, divisor):
    dividend = np.array(dividend, dtype=float)
    divisor = np.array(divisor, dtype=float)
    quotient = np.zeros(len(dividend) - len(divisor) + 1)
    remainder = np.copy(dividend)
    while len(remainder) >= len(divisor):
        lead_coeff = remainder[0] / divisor[0]
        degree_diff = len(remainder) - len(divisor)
        quotient[degree_diff] = lead_coeff
        subtract_term = np.zeros_like(remainder)
        subtract_term[:len(divisor)] = lead_coeff * divisor
        remainder = np.subtract(remainder, subtract_term)
        remainder = np.trim_zeros(remainder, 'f')
    return quotient, remainder

def poly_gcd_extended(a, b):
    if all(coef == 0 for coef in b):
        return a, [1], [0]
    quotient, remainder = poly_divide(a, b)
    gcd, x1, y1 = poly_gcd_extended(b, remainder)
    x = y1
    y = np.polyadd(np.polymul(-np.array(quotient), np.array(y1)), np.array(x1)).tolist()
    return gcd, x, y

def solve_diophantine(f, g):
    gcd, A, B = poly_gcd_extended(f, g)
    gcd = np.trim_zeros(np.array(gcd), 'f').tolist()
    A = np.trim_zeros(np.array(A), 'f').tolist()
    B = np.trim_zeros(np.array(B), 'f').tolist()
    return gcd, A, B

f = [1, 0, 1]  # f(x) = x^2 + 1
g = [1, 0, -1]  # g(x) = x^2 - 1

gcd, A, B = solve_diophantine(f, g)
print("gcd:", gcd)
print("A:", A)
print("B:", B)
