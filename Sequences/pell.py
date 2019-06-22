# pell.py
# f(x) = 2x + 1

from Sequences.sequence import sequence


def pell(number_of_terms):
    seq = sequence(number_of_terms, 0, 1, multiplier_first_term=1, multiplier_second_term=2, constant_factor=0)
    return seq


def main():
    p = pell(100)
    print(p)


if __name__ == "__main__":
    main()
