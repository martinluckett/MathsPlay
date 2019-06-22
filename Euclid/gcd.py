# gcd.py
#
#  Greatest Common Divisor using Euclid's Algorithm
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def main():
    result = gcd(252, 105)
    print(result)


if __name__ == "__main__":
    main()


