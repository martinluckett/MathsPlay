# pell.py
#
#  Pell Numbers
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019

from Sequences.sequence import sequence


def pell(number_of_terms=100):

    result = sequence(number_of_terms=number_of_terms,
                      first_term=0,
                      second_term=1,
                      multiplier_first_term=1,
                      multiplier_second_term=2)

    return result


def main():
    pel = pell(100)
    print("Pell", pel)


if __name__ == "__main__":
    main()