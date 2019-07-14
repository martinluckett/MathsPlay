# nCk.py
#
#  n items, choose k
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019
from Basics.factorial import factorial


def nCk(n, k):

    result = factorial(n) / (factorial(k) * factorial(n - k))

    return int(result)


def main():
    n = 100
    k = 4
    a = nCk(n, k)

    print(a)


if __name__ == "__main__":
    main()
