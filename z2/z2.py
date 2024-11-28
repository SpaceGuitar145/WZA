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

def poly_multiply(poly1, poly2):
    result = [0] * (len(poly1) + len(poly2) - 1)
    for i, coeff1 in enumerate(poly1):
        for j, coeff2 in enumerate(poly2):
            result[i + j] += coeff1 * coeff2
    return result

def poly_lcm(poly1, poly2):
    gcd = poly_gcd(poly1, poly2)
    multiplied_poly = poly_multiply(poly1, poly2)
    lcm, _ = poly_divide(multiplied_poly, gcd)
    return lcm

dividend = [1, 0, 1]
divisor = [1, 0, -1]
quotient, remainder = poly_divide(dividend, divisor)
print("Quotient:", quotient)
print("Remainder:", remainder)

gcd = poly_gcd(dividend, divisor)
print("GCD:", gcd)

lcm = poly_lcm(dividend, divisor)
print("LCM:", lcm)
