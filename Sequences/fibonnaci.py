# fibonacci.py
#
#  Fibonacci Numbers
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019

from Sequences.sequence import sequence


def fibonacci(number_of_terms=100):

    result = sequence(number_of_terms=number_of_terms,
                      first_term=0,
                      second_term=1)

    return result


def main():
    fib = fibonacci(100)
    print("Fibonacci", fib)


if __name__ == "__main__":
    main()