from Sequences.fibonacci import fibonacci
from Sequences.lucas import lucas
from Sequences.mersenne import mersenne
from mathsConstants.goldenratio import phi
from mathsConstants.goldenratio_fibonacci import gr_fibonacci


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

    print("Fibonacci Numbers:\n ", fib)
    print("Lucas Numbers:\n", luc)
    print("Mersenne Numbers:\n", mer)
    print("Golden Ratio:\n", gr)
    print("Golden Ratio using Fibonacci Numbers:\n", gr_fib)


def main():
    tests()


if __name__ == "__main__":
    main()
