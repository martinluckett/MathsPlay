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
    nth_term = 50

    fib = Fibonacci()
    fib.test(number_of_terms, nth_term)

    luc = Lucas()
    luc.test(number_of_terms, nth_term)

    mer = Mersenne()
    mer.test(number_of_terms, nth_term)

    pel = Pell()
    pel.test(number_of_terms, nth_term)

    coll = Collatz(100)
    coll.test()

    coll = Collatz(1000)
    coll.test()


def main():
    basic_tests()
    sequence_tests()


if __name__ == "__main__":
    main()
