# link: https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem

"""PSEUDOCODE
CLASS: Complex
    ATTRIBUTES:
        1. real: float
        2. imag: float

    METHODS:
        1. Constructor(str) -> Complex
        2. Add (a: Complex, b: Complex) -> Sum: Complex
        3. Subtract(a: Complex, b: Complex) -> Difference: Complex      // consider positive or negative difference
        4. Multiply (a: Complex, b: Complex) -> Product: Complex
        5. Divide (a: Complex, b: Complex) -> Quotient: Complex     // consider division by zero, etc.
        6. Mod (a: Complex) -> ??
        7. __str__
"""


class Complex:
    def __init__(self, num_str):
        self.real, self.imag = map(float, num_str.split())

    def __add__(num1, num2):
        result = Complex(f"{num1.real + num2.real} {num1.imag + num2.imag}")
        return result

    def __sub__(num1, num2):
        result = Complex(f"{num1.real - num2.real} {num1.imag - num2.imag}")
        return result

    def __mul__(num1, num2):
        result = Complex(f"{(num1.real * num2.real) - (num1.imag * num2.imag)} {(num1.real * num2.imag) + (num1.imag * num2.real)}")
        return result

    def div(self):
        pass
