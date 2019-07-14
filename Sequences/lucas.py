# lucas.py
#
#  Lucas Numbers
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019

from Sequences.sequence import sequence


def lucas(number_of_terms=100):

    result = sequence(number_of_terms=number_of_terms,
                      first_term=2,
                      second_term=1)

    return result


def main():
    luc = lucas(100)
    print("Lucas", luc)


if __name__ == "__main__":
    main()