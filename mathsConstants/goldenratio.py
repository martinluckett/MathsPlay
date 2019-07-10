# goldenratio.py
#
#  Algebraic form of the golden ratio
#  PHI = 1/2 * (1 + SQRT(5))
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019

from decimal import *
from Sequences.sequence import fibonacci
from Sequences.sequence import ratio_at_final_term


def phi(precision=20):
    # Using Decimal
    getcontext().prec = precision
    result = (Decimal(0.5)*(Decimal(1) + Decimal(5).sqrt()))
    return result


def gr_fibonacci(n, precision=20):
    fib = fibonacci(number_of_terms=n)
    result = ratio_at_final_term(fib, precision)
    return result


def main():
    precision = 20

    gr = phi(precision)
    print(gr)

    number_of_terms = 100
    fib_ratio = gr_fibonacci(number_of_terms, precision)
    print(fib_ratio)


if __name__ == "__main__":
    main()