class GaussianInteger:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def norm(self):
        norm_value = self.real**2 + self.imag**2
        return norm_value

    def __mul__(self, other):
        result = GaussianInteger(self.real * other.real - self.imag * other.imag,
                                 self.real * other.imag + self.imag * other.real)
        return result

    def divide(self, divisor):
        divisor_norm = divisor.norm()
        real_part = int((self.real * divisor.real + self.imag * divisor.imag) / divisor_norm)
        imag_part = int((self.imag * divisor.real - self.real * divisor.imag) / divisor_norm)
        return GaussianInteger(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

def subtract_product(a, b, scalar):
    result = GaussianInteger(a.real - b.real * scalar, a.imag - b.imag * scalar)
    return result

def gcd(a, b):
    while b.norm() != 0:
        division = a.divide(b)
        
        r = subtract_product(a, b, division.real)
        r = subtract_product(r, GaussianInteger(-b.imag, b.real), division.imag)
        
        a, b = b, r
    return a

def lcm(a, b):
    product = a * b
    gcd_result = gcd(a, b)
    result = product.divide(gcd_result)
    return result

def main():
    a = GaussianInteger(3, 4)
    b = GaussianInteger(1, 3)

    div_result = a.divide(b)
    gcd_result = gcd(a, b)
    lcm_result = lcm(a, b)

    print(f"Division of {a} and {b} is: {div_result}")
    print(f"GCD of {a} and {b} is: {gcd_result}")
    print(f"LCM of {a} and {b} is: {lcm_result}")

if __name__ == '__main__':
    main()
