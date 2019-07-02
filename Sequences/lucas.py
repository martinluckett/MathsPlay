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

    def generate_sequence(self, number_of_terms=100):
        result = []
        a = self.first_term
        b = self.second_term

        result.append(a)

        while len(result) < number_of_terms + 1:
            # add b to the list
            result.append(b)
            # new a = old b, new b = calculated term
            a, b = b, a + b

        self.seq = result

