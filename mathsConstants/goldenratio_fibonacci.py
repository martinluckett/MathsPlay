# goldenratio_fibonacci.py
#
#  Calculate the golden ratio using the nth term of the Fibonacci Sequence
#
#  As n -> infinity , F(n)/F(n-1) tends to the golden ratio
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019

from Sequences.fibonacci import fibonacci
from decimal import *


def gr_fibonacci(n, precision):
    getcontext().prec = precision
    fib = fibonacci(n)
    nth_term = Decimal(fib[n])
    previous_term = Decimal(fib[n - 1])
    result = (nth_term/previous_term)
    return result


def main():
    res = gr_fibonacci(1000, 100)
    print(res)


if __name__ == "__main__":
    main()