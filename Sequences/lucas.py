# lucas.py
# Generate the Lucas Numbers for a defined number of terms
#
# The Lucas Numbers are a sequence such that each number is the sum of the
# two preceding ones, starting from 2 and 1
# F(0) = 0, F(1) = 1
# F(n) = F(n-1) + F(n-2), for n > 1
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019


from Sequences.sequence import Sequence


class Lucas(Sequence):
    def __init__(self):
        super().__init__(first_term=2, second_term=1, name="Lucas")

