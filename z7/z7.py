def poly_divide(dividend, divisor):
    remainder = list(dividend)

    divisor_degree = len(divisor) - 1
    remainder_degree = len(remainder) - 1

    quotient = [0] * (remainder_degree - divisor_degree + 1)

    while remainder_degree >= divisor_degree and any(remainder):
        scale = remainder[remainder_degree] / divisor[divisor_degree]
        quotient[remainder_degree - divisor_degree] = scale

        for i in range(divisor_degree + 1):
            remainder[remainder_degree - i] -= scale * divisor[divisor_degree - i]

        while remainder_degree >= 0 and remainder[remainder_degree] == 0:
            remainder.pop()
            remainder_degree -= 1

    return quotient, remainder

def poly_gcd(a, b):
    while b:
        _, remainder = poly_divide(a, b)
        a, b = b, remainder
    return a

def poly_gcd_three(a, b, c):
    gcd_ab = poly_gcd(a, b)
    gcd_abc = poly_gcd(gcd_ab, c)
    return gcd_abc

poly1 = [1, 0, 1, 0, 1]
poly2 = [1, 0, -1, -2, -1]
poly3 = [1, 0, 0, 0, -1]

poly4 = [1, 1, -4, -4]
poly5 = [1, -1, -4, 4]
poly6 = [1, -2, -1, 2]

gcd_result1 = poly_gcd_three(poly1, poly2, poly3)
gcd_result2 = poly_gcd_three(poly4, poly5, poly6)

print("GCD of the three polynomials is (1):", gcd_result1)
print("GCD of the three polynomials is (2):", gcd_result2)
