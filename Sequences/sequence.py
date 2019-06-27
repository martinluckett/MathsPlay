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


class Sequence:
    def __init__(self, first_term, second_term, name="default",
                 multiplier_first_term=1, multiplier_second_term=1,
                 exponent_first_term=1, exponent_second_term=1,
                 constant_factor=0):
        self.first_term = first_term
        self.second_term = second_term
        self.name = name
        self.multiplier_first_term = multiplier_first_term
        self.multiplier_second_term = multiplier_second_term
        self.exponent_first_term = exponent_first_term
        self.exponent_second_term = exponent_second_term
        self.constant_factor = constant_factor

        self.seq = []

    def generate_sequence(self, number_of_terms=100):

        result = []
        a = self.first_term
        b = self.second_term
        c = self.multiplier_first_term
        d = self.multiplier_second_term
        e = self.exponent_first_term
        f = self.exponent_second_term
        g = self.constant_factor

        # add the first term
        result.append(a)

        # generate the sequence
        while len(result) < number_of_terms + 1:
            # add b to the list
            result.append(b)
            # new a = old b, new b = calculated term
            a, b = b, (c * (a ** e)) + (d * (b ** f)) + g

        self.seq = result

    def nth_term(self, nth_term):
        if nth_term > len(self.seq):
            self.generate_sequence(nth_term)

        return self.seq[nth_term]

    def ratio_at_nth_term(self, n, precision=20):
        if n > len(self.seq):
            self.generate_sequence(n)

        getcontext().prec = precision
        nth = Decimal(self.nth_term(n))
        previous_term = Decimal(self.nth_term(n-1))
        result = (nth / previous_term)
        return result

    def output_sequence(self, number_of_terms=100):
        print("The first {n} terms of the {name} sequence:".format(n=number_of_terms, name=self.name))
        print(self.seq, "\n")













#
# seq_test_number_terms = 100


