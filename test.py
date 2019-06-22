from Sequences.fibonacci import fibonacci
from Sequences.lucas import lucas
from Sequences.mersenne import mersenne
from GoldenRatio.goldenratio import phi
from GoldenRatio.goldenratio_fibonacci import gr_fibonacci


def tests():
    # Fibonacci Sequence.  Argument is the number of terms
    fib = fibonacci(100)

    # Lucas Numbers. Argument is the number of terms
    luc = lucas(100)

    # Mersenne Numbers. Argument is the number of terms
    mer = mersenne(100)

    # Golden Ratio. Argument is the number of decimal places
    gr = phi(100)

    # Golden Ratio using Fibonacci Numbers
    # arguments are (nth fibonacci term to use, number of decimal places)
    # higher n gives greater accuracy
    gr_fib = gr_fibonacci(n=100, precision=100)


    print("Fibonacci Numbers:\n ", fib)
    print("Lucas Numbers:\n", luc)
    print("Mersenne Numbers:\n", mer)
    print("Golden Ratio:\n", gr)
    print("Golden Ratio using Fibonacci Sequence:\n", gr_fib)


def main():
    tests()


if __name__ == "__main__":
    main()
