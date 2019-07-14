# tests.py
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019


from Basics.gcd import gcd
from Basics.gcd import gcd_recursive
from primes.coprime import coprime
from Sequences.fibonnaci import fibonacci
from Sequences.lucas import lucas
from Sequences.mersenne import mersenne
from Sequences.pell import pell
from Sequences.collatz import collatz
from mathsConstants.goldenratio import gr_fibonacci
from mathsConstants.goldenratio import phi


def basic_tests():
    # Greatest Common Divisor
    # Arguments are the two numbers for which the gcd needs to be found
    # Recursive version likely to need fewer steps for larger numbers
    # Example usage: gcd(252, 105) using the subtractive method function
    # Example usage: gcd_recursive(252, 105) using the recursive mod function

    gcd_str = "Greatest Common Divisor of {n1} and {n2} is {result} (using {method})\n"

    print(gcd_str.format(n1=252, n2=105, result=gcd(252, 105), method="subtractive method"))
    print(gcd_str.format(n1=252, n2=105, result=gcd_recursive(252, 105), method="recursive mod function"))

    # Coprime test
    # Arguments are the two numbers to be checked
    # Returns True or False
    # Example: coprime(6, 35)

    coprime_str = "{n1} and {n2} are coprime is: {result}\n"
    print(coprime_str.format(n1=6, n2=35, result=coprime(6, 35)))


def sequence_tests():
    number_of_terms = 100

    fib = fibonacci(number_of_terms)
    print("Fibonacci", fib)

    luc = lucas(number_of_terms)
    print("Lucas", luc)

    mer = mersenne(number_of_terms)
    print("Mersenne", mer)

    pel = pell(number_of_terms)
    print("Pell", pel)

    n = 100
    col = collatz(n)
    print("Collatz: {0} reached 1 in {1} steps".format(n, col))


def golden_ratio_test():
    precision = 50

    gr = phi(precision)

    number_of_terms = 100
    gr_fib = gr_fibonacci(number_of_terms, precision)

    print("\nGolden Ratio\n")
    print("Algebraic\n", gr)
    print("Using {0} terms of the Fibonacci Sequence\n {1}".format(number_of_terms, gr_fib))


def main():
    basic_tests()
    sequence_tests()
    golden_ratio_test()


if __name__ == "__main__":
    main()
