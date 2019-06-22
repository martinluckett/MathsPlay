# fibonacci.py
# Generate the Fibonacci Numbers for a defined number of terms
#
# The Fibonacci Numbers are a sequence such that each number is the sum of the
# two preceding ones, starting from 0 and 1
# F(0) = 0, F(1) = 1
# F(n) = F(n-1) + F(n-2), for n > 1
#
# Update: created generalised sequence generator and moved to sequence.py
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019

from sequences.sequence import sequence


def fibonacci(number_of_terms):
    seq = sequence(number_of_terms, first_term=0, second_term=1)
    return seq


def main():
    # Set the number of terms to be calculated
    number_of_terms = 100

    # Call the sequence function with the fibonacci parameters
    f = fibonacci(number_of_terms)

    print(f)


if __name__ == "__main__":
    main()
