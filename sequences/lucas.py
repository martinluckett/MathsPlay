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

from Sequences.sequences import sequence


def lucas(number_of_terms):
    seq = sequence(number_of_terms, first_term=2, second_term=1)
    return seq


def main():
    # Set the number of terms to be calculated
    number_of_terms = 100

    # Call the sequence function with the lucas parameters
    f = lucas(number_of_terms)

    print(f)


if __name__ == "__main__":
    main()
