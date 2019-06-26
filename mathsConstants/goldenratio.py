# goldenratio.py
#
#  Algebraic form of the golden ratio
#  PHI = 1/2 * (1 + SQRT(5))
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019

from decimal import *
from Sequences.fibonacci import Fibonacci


def phi(precision=20):
    # Using Decimal
    getcontext().prec = precision
    result = (Decimal(0.5)*(Decimal(1) + Decimal(5).sqrt()))
    return result


def gr_fibonacci(n, precision):
    fib = Fibonacci()
    result = fib.ratio_at_nth_term(n, precision)
    return result


def main():
    gr = phi(100)
    print(gr)
    res = gr_fibonacci(n=100, precision=100)
    print(res)
    diff = res - gr
    print(diff / gr * 100, "%")


if __name__ == "__main__":
    main()