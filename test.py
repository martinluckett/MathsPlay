# tests.py
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019


from Basics.gcd import gcd
from Basics.gcd import gcd_recursive
from primes.coprime import coprime
from Sequences.fibonacci import Fibonacci
from Sequences.lucas import Lucas
from Sequences.mersenne import Mersenne
from Sequences.pell import Pell
from Sequences.collatz import Collatz


def basic_tests():
    # Greatest Common Divisor
    # Arguments are the two numbers for which the gcd needs to be found
    # Recursive version likely to need fewer steps for larger numbers
    gcd(252, 105)
    gcd_recursive(252, 105)

    # Coprime test
    # Arguments are the two numbers to be checked
    # Returns True or False
    coprime(6, 35)

    print("Greatest Common Divisor of {0} and {1} is {2} (using subtractive method)\n"
          .format(252, 105, gcd(252, 105)))
    print("Greatest Common Divisor of {0} and {1} is {2} (using recursive mod function)\n"
          .format(252, 105, gcd_recursive(252, 105)))
    print("{0} and {1} are coprime is: {2}\n".format(6, 35, coprime(6, 35)))


def sequence_tests():
    number_of_terms = 100
    nth_term = 50

    fib = Fibonacci()
    fib.test(number_of_terms, nth_term)

    luc = Lucas()
    luc.test(number_of_terms, nth_term)

    mer = Mersenne()
    mer.test(number_of_terms, nth_term)

    pel = Pell()
    pel.test(number_of_terms, nth_term)

    coll = Collatz(1000)
    print("For n = {0} the Collatz sequence reaches 1 in {1} steps".format(coll.initial_number, coll.counter))


def main():
    basic_tests()
    sequence_tests()


if __name__ == "__main__":
    main()
