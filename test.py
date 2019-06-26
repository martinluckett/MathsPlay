from mathsConstants.goldenratio import phi
from Euclid.gcd import gcd
from Euclid.gcd import gcd_recursive
from primes.coprime import coprime


def main():
    # Greatest Common Divisor
    # Arguments are the two numbers for which the gcd needs to be found
    # Recursive version likely to need fewer steps for larger numbers
    gcd(252, 105)
    gcd_recursive(252, 105)

    # Coprime test
    # Arguments are the two numbers to be checked
    # Returns True or False
    coprime(6, 35)



    print("\nGreatest Common Divisor of {0} and {1} is {2} (using subtractive method)\n"
          .format(252, 105, gcd(252, 105)))
    print("\nGreatest Common Divisor of {0} and {1} is {2} (using recursive mod function)\n"
          .format(252, 105, gcd_recursive(252, 105)))
    print("\n{0} and {1} are coprime is: {2}\n".format(6, 35, coprime(6, 35)))


if __name__ == "__main__":
    main()
