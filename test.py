from mathsConstants.goldenratio import phi
from Basics.gcd import gcd
from Basics.gcd import gcd_recursive
from primes.coprime import coprime
from Sequences.fibonacci import Fibonacci
from Sequences.lucas import Lucas
from Sequences.mersenne import Mersenne
from Sequences.pell import Pell


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
    nth_term_str = "Term {n} of the {name} sequence is: {result}\n"
    nth_term_ratio_str = "The ratio of consecutive terms at term {n} of the {name} sequence is: {result}\n"

    fib = Fibonacci()
    fib.output_sequence(number_of_terms)
    print(nth_term_str.format(n=nth_term, name=fib.name, result=fib.nth_term(nth_term)))
    print(nth_term_ratio_str.format(n=nth_term, name=fib.name, result=fib.ratio_at_nth_term(nth_term)))

    luc = Lucas()
    luc.output_sequence(number_of_terms)
    print(nth_term_str.format(n=nth_term, name=luc.name, result=luc.nth_term(nth_term)))
    print(nth_term_ratio_str.format(n=nth_term, name=luc.name, result=luc.ratio_at_nth_term(nth_term)))

    mer = Mersenne()
    mer.output_sequence(number_of_terms)
    print(nth_term_str.format(n=nth_term, name=mer.name, result=mer.nth_term(nth_term)))
    print(nth_term_ratio_str.format(n=nth_term, name=mer.name, result=mer.ratio_at_nth_term(nth_term)))

    pel = Pell()
    pel.output_sequence(number_of_terms)
    print(nth_term_str.format(n=nth_term, name=pel.name, result=pel.nth_term(nth_term)))
    print(nth_term_ratio_str.format(n=nth_term, name=pel.name, result=pel.ratio_at_nth_term(nth_term)))


def main():
    basic_tests()
    sequence_tests()


if __name__ == "__main__":
    main()
