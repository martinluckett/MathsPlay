# fibonacci.py
# Generate the Fibonacci Numbers for a defined number of terms
#
# The Fibonacci Numbers are a sequence such that each number is the sum of the
# two preceding ones, starting from 0 and 1
# F(0) = 0, F(1) = 1
# F(n) = F(n-1) + F(n-2), for n > 1
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019

from Sequences.sequence import Sequence


class Fibonacci(Sequence):
    def __init__(self):
        super().__init__(first_term=0, second_term=1, name="Fibonacci")



