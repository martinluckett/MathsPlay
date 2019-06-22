from Sequences.fibonacci import fibonacci
from Sequences.lucas import lucas
from Sequences.mersenne import mersenne
from mathsConstants.goldenratio import phi
from mathsConstants.goldenratio_fibonacci import gr_fibonacci
from Euclid.gcd import gcd
from Euclid.gcd import gcd_recursive
from primes.coprime import coprime


def tests():
    # Fibonacci Numbers
    # argument is the number of terms
    fib = fibonacci(100)

    # Lucas Numbers
    # argument is the number of terms
    luc = lucas(100)

    # Mersenne Numbers
    # argument is the number of terms
    mer = mersenne(100)

    # Golden Ratio
    # argument is the number of decimal places
    gr = phi(100)

    # Golden Ratio using Fibonacci Numbers
    # arguments are (nth fibonacci term to use, number of decimal places)
    # higher n gives greater accuracy
    gr_fib = gr_fibonacci(n=100, precision=100)

    # Greatest Common Divisor
    # Arguments are the two numbers for which the gcd needs to be found
    # Recursive version likely to need fewer steps for larger numbers
    gcd(252, 105)
    gcd_recursive(252, 105)

    # Coprime test
    # Arguments are the two numbers to be checked
    # Returns True or False
    coprime(6, 35)

    print("Fibonacci Numbers:\n ", fib)
    print("\nLucas Numbers:\n", luc)
    print("\nMersenne Numbers:\n", mer)
    print("\nGolden Ratio:\n", gr)
    print("\nGolden Ratio using Fibonacci Numbers:\n", gr_fib)
    print("\nGreatest Common Divisor of {0} and {1} is {2} (using subtractive method)\n"
          .format(252, 105, gcd(252, 105)))
    print("\nGreatest Common Divisor of {0} and {1} is {2} (using recursive mod function)\n"
          .format(252, 105, gcd_recursive(252, 105)))
    print("\n{0} and {1} are coprime is: {2}\n".format(6, 35, coprime(6, 35)))


def main():
    tests()


if __name__ == "__main__":
    main()
