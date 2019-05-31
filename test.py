from Sequences.fibonacci import fibonacci
from Sequences.lucas import lucas


def sequence_test():
    fib = fibonacci(100)
    luc = lucas(100)

    print("Fibonacci Numbers:\n ", fib)
    print("Lucas Numbers:\n", luc)


def main():
    sequence_test()


if __name__ == "__main__":
    main()
