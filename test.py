from Sequences.fibonacci import fibonacci
from Sequences.lucas import lucas
from Sequences.mersenne import mersenne
from GoldenRatio.goldenratio import phi


def sequence_test():
    fib = fibonacci(100)
    luc = lucas(100)
    mer = mersenne(100)
    gr = phi(100)

    print("Fibonacci Numbers:\n ", fib)
    print("Lucas Numbers:\n", luc)
    print("Mersenne Numbers:\n", mer)
    print("Golden Ratio:\n", gr)


def main():
    sequence_test()


if __name__ == "__main__":
    main()
