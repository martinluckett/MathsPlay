# lucas.py
# Generate the Lucas Numbers for a defined number of terms
#
# The Lucas Numbers are a sequence such that each number is the sum of the
# two preceding ones, starting from 2 and 1
# F(0) = 0, F(1) = 1
# F(n) = F(n-1) + F(n-2), for n > 1
#
# The number of terms is specified in the main() function as number_of_terms
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019

from sequences import sequence
from sequences import output_all_to_screen
from sequences import output_all_to_file
from sequences import nth_term
from sequences import run_time_str
from sequences import filename_str
from sequences import nth_term_str
import time


def main():
    # Name of Sequence
    sequence_str = "Lucas"

    # Set the number of terms to be calculated
    number_of_terms = 100

    start_time = time.time()
    seq = sequence(number_of_terms, first_term=2, second_term=1)
    run_time = str(time.time() - start_time)

    print("\n{0} Sequence".format(sequence_str))
    output_all_to_screen(seq)

    filename = filename_str.format(sequence_str, number_of_terms)
    # output_all_to_file(seq, filename)

    print(run_time_str.format(sequence_str, run_time))

    # Print the (n)th term of the sequence
    n = 100

    print(nth_term_str.format(n, sequence_str, nth_term(seq, n)))


if __name__ == "__main__":
    main()
