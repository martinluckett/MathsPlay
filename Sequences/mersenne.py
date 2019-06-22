# mersenne.py
# f(x) = 2x + 1

from Sequences.sequence import sequence


def mersenne(number_of_terms):
    seq = sequence(number_of_terms, 0, 1, multiplier_first_term=0, multiplier_second_term=2, constant_factor=1)
    return seq


def main():
    m = mersenne(100)
    print(m)


if __name__ == "__main__":
    main()
