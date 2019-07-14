# sequences.py
#
# create a sequence such with initial terms: first_term and second_term
# generate new terms by:
#
# new term = (first_term ** (exponent)) * (multiplier)
#               + (second_term ** (exponent)) * (multiplier)
#               + constant_factor
#
# default multiplier is 1
# default exponent is 1
# default constant is 0
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019

from decimal import *


def sequence(number_of_terms, first_term=0, second_term=1,
             multiplier_first_term=1, multiplier_second_term=1,
             exponent_first_term=1, exponent_second_term=1, constant_factor=0):

    result = []

    a = first_term
    b = second_term
    c = multiplier_first_term
    d = multiplier_second_term
    e = exponent_first_term
    f = exponent_second_term
    g = constant_factor

    # print(a,b, c, d, e, f, g)

    # add the first term
    result.append(a)

    # generate the sequence
    while len(result) < number_of_terms + 1:
        result.append(b)

        # new a = old b, new b = calculated term
        a, b = b, (c * (a ** e)) + (d * (b ** f)) + g

    return result


def ratio_at_final_term(seq, precision=20):
    n = len(seq)
    getcontext().prec = precision
    final_term = Decimal(seq[n-1])
    previous_term = Decimal(seq[n-2])
    result = (final_term / previous_term)
    return result


def test():
    pass


if __name__ == "__main__":
    test()
