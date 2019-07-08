# pell.py
# f(x) = ...
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019

from Sequences.sequence import Sequence


class Pell(Sequence):
    def __init__(self):
        super().__init__(first_term=0, second_term=1, name="Pell",
                         multiplier_first_term=1, multiplier_second_term=2)

