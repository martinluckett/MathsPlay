# mersenne.py
# f(x) = 2x + 1

from sequences.sequence import seq


def mersenne(number_of_terms):
    result = seq(number_of_terms, 0, 1, multiplier_first_term=0, multiplier_second_term=2, constant_factor=1)
    return result


def main():
    m = mersenne(100)
    print(m)


if __name__ == "__main__":
    main()
