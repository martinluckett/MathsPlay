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

import time

error_str = "Error: {0}"


def fibonacci(n):
    # generate fibonacci sequence to the (n)th term
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(b)
        a, b = b, a+b
    return sequence


def output_all_to_screen(sequence):
    print("n", "Fibonacci Sequence")
    for i in range(0, len(sequence)):
        print(i+1, sequence[i])


def output_all_to_file(sequence, filename):
    try:
        with open(filename, "w") as file:
            for i in range(0, len(sequence)):
                fib_str = "{0} {1}\n".format(i+1, sequence[i])
                file.write(fib_str)
    except IOError as e:
        print(error_str.format(e))
    except TypeError as e:
        print(error_str.format(e))


def nth_term(sequence, n):
    try:
        result = sequence[n-1]
    except IndexError as e:
        print(error_str.format(e))
    else:
        return result


def main():
    number_of_terms = 100
    start_time = time.time()
    f = fibonacci(number_of_terms)
    run_time = str(time.time() - start_time)

    # Note: for long sequences, outputting the list to the screen can slow things down considerably
    # Uncomment line below to use
    # output_all_to_screen(f)

    output_all_to_file(f, "fib_100.txt")

    # Print the (n)th term of the sequence
    n = 99
    print("The {0}th term is {1}".format(n, nth_term(f, n)))

    print("run time: {0} seconds".format(run_time))


if __name__ == "__main__":
    main()