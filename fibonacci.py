# fibonacci.py
# Generate the Fibonacci Numbers for a defined number of terms
#
# The Fibonacci Numbers are a sequence such that each number is the sum of the
# two preceding ones, starting from 0 and 1
# F(0) = 0, F(1) = 1
# F(n) = F(n-1) + F(n-2), for n > 1
#
# The number of terms is specified in the main() function as number_of_terms
# The nth term can be examined by altering the variable n in the main() function
#
# Update: generalised sequence generator so that it can start with any two terms to generate other sequences
# e.g. Lucas numbers which start with 2 and 1.
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019

import time

error_str = "Error: {0}"


def sequence(n, first_term, second_term):
    # generate sequence to the (n)th term
    seq = []
    # Set the first two terms
    a, b = first_term, second_term
    seq.append(a)
    # Generate the sequence by adding the two previous terms
    while len(seq) < n+1:
        seq.append(b)
        a, b = b, a+b
    return seq


def output_all_to_screen(seq):
    print("n", "Sequence")
    for i in range(0, len(seq)):
        print("{0} {1}".format(i, seq[i]))


def output_all_to_file(seq, filename):
    try:
        with open(filename, "w") as file:
            for i in range(0, len(seq)):
                seq_str = "{0} {1}\n".format(i, seq[i])
                file.write(seq_str)
    except IOError as e:
        print(error_str.format(e))
    except TypeError as e:
        print(error_str.format(e))


def nth_term(seq, n):
    try:
        result = seq[n]
    except IndexError as e:
        print(error_str.format(e))
    else:
        return result


def main():
    # Set the number of terms to be calculated
    number_of_terms = 100

    # Fibonacci Numbers
    fib_start_time = time.time()
    fib_seq = sequence(number_of_terms, 0, 1)
    fib_run_time = str(time.time() - fib_start_time)

    # Note: for long sequences, outputting the list to the screen can slow things down considerably
    # Uncomment lines below to use
    print("\nFibonacci Numbers")
    output_all_to_screen(fib_seq)

    # Output the sequence to a txt file
    # Uncomment the two lines below to use
    # filename = "fib_100.txt"
    # output_all_to_file(fib_seq, filename)

    # Lucas Numbers
    luc_start_time = time.time()
    luc_seq = sequence(number_of_terms, 2, 1)
    luc_run_time = str(time.time() - luc_start_time)

    print("\nLucas Numbers")
    output_all_to_screen(luc_seq)
    # output_all_to_file(luc_seq, "luc_100.txt")

    # Print run times of sequence calculations
    run_time_str = "{0} numbers run time: {1} seconds"

    print(run_time_str.format("Fibonacci", fib_run_time))
    print(run_time_str.format("Lucas", luc_run_time))

    # Print the (n)th term of the sequence
    n = 100

    nth_term_str = "The {0}th term of the {1} numbers is {2}"

    print(nth_term_str.format(n, "Fibonacci", nth_term(fib_seq, n)))
    print(nth_term_str.format(n, "Lucas", nth_term(luc_seq, n)))


if __name__ == "__main__":
    main()
