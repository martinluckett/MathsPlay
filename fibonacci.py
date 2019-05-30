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

    start_time = time.time()
    f = sequence(number_of_terms, 0, 1)
    run_time = str(time.time() - start_time)

    # Note: for long sequences, outputting the list to the screen can slow things down considerably
    # Uncomment line below to use
    # output_all_to_screen(f)

    # Output the sequence to a txt file
    # Uncomment the two lines below to use
    # filename = "fib_100.txt"
    # output_all_to_file(f, filename)

    # Print the (n)th term of the sequence
    n = 99
    print("The {0}th term is {1}".format(n, nth_term(f, n)))

    print("run time: {0} seconds".format(run_time))


if __name__ == "__main__":
    main()
