from Sequences.fibonacci import fibonacci
from Sequences.lucas import lucas
from Sequences.mersenne import mersenne
from GoldenRatio.goldenratio import phi
from GoldenRatio.goldenratio_fibonacci import gr_fibonacci


def sequence_test():
    fib = fibonacci(100)  # argument is the number of terms
    luc = lucas(100)  # argument is the number of terms
    mer = mersenne(100)  # argument is the number of terms
    gr = phi(100)  # argument is the number of decimal places
    gr_fib = gr_fibonacci(1000, 100)  # arguments are (nth fibonacci term to use, number of decimal places)

    print("Fibonacci Numbers:\n ", fib)
    print("Lucas Numbers:\n", luc)
    print("Mersenne Numbers:\n", mer)
    print("Golden Ratio:\n", gr)
    print("Golden Ratio using Fibonacci Sequence:\n", gr_fib)


def main():
    sequence_test()


if __name__ == "__main__":
    main()
