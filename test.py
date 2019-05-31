from Sequences.fibonacci import fibonacci
from Sequences.lucas import lucas
from Sequences.mersenne import mersenne


def sequence_test():
    fib = fibonacci(100)
    luc = lucas(100)
    mer = mersenne(100)

    print("Fibonacci Numbers:\n ", fib)
    print("Lucas Numbers:\n", luc)
    print("Mersenne Numbers:\n", mer)


def main():
    sequence_test()


if __name__ == "__main__":
    main()
