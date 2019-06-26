# mersenne.py
# f(x) = 2x + 1
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019


from Sequences.sequence import Sequence


class Mersenne(Sequence):
    def __init__(self):
        super().__init__(first_term=0, second_term=1, name="Mersenne",
                         multiplier_first_term=0, multiplier_second_term=2,
                         constant_factor=1)

