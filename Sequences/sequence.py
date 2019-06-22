# sequences.py
#
# create a sequence such with initial terms: first_term and second_term
# generate new terms by:
#
# new term = (first_term)*(first_term_multiplier) + (second_term**(exponent))*(second_term_multiplier) + constant_factor
#
# default multiplier is 1
# default exponent is 1
# default constant is 0
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019


def seq(n, first_term, second_term,
        multiplier_first_term=1, multiplier_second_term=1,
        exponent_second_term=1, constant_factor=0):

    # Create an empty list to hold the results
    seq_list = []

    # Set the first two terms
    a, b = first_term, second_term

    # Set the multipliers and exponents for the terms (default = 1)
    c, d, e = multiplier_first_term, multiplier_second_term, exponent_second_term

    # Set the constant to be added (default = 0)
    f = constant_factor

    # Add the first term to the sequence result
    seq_list.append(a)

    # Generate the sequence until the length of the sequence is n terms
    while len(seq_list) < n+1:
        # add b to the list
        seq_list.append(b)
        # new a = old b, new b = calculated term
        a, b = b, (c*a)+(d*(b**e)) + f

    # Return the sequence of n terms
    return seq_list


