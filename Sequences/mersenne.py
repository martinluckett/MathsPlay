# fibonacci.py
#
#  Mersenne Numbers
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019

from Sequences.sequence import sequence


def mersenne(number_of_terms=100):

    result = sequence(number_of_terms=number_of_terms,
                      first_term=0,
                      second_term=1,
                      multiplier_first_term=0,
                      multiplier_second_term=2,
                      constant_factor=1)

    return result
