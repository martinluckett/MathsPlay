from fibonacci import fibonacci
from lucas import lucas


def main():
    fib = fibonacci(100)
    luc = lucas(100)

    print("Fibonacci Numbers:\n ", fib)
    print("Lucas Numbers:\n", luc)


if __name__ == "__main__":
    main()
