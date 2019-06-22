# goldenratio_fibonacci.py
#
#  Calculate the golden ratio using the nth term of the Fibonacci Sequence
#
#  As n -> infinity , 1 + F(n)/F(n-1) tends to the golden ratio
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019

from Sequences.fibonacci import fibonacci
from decimal import *


def gr_fibonacci(n, precision):
    getcontext().prec = precision
    fib = fibonacci(n)
    first_term = Decimal(fib[n-1])
    second_term = Decimal(fib[n])
    result = 1 + (first_term/second_term)
    return result


def main():
    res = gr_fibonacci(1000, 100)
    print(res)


if __name__ == "__main__":
    main()