# goldenratio.py
#
#  PHI = 1/2 * (1 + SQRT(5))
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019

import math
from decimal import *


def phi(precision=20):
    # Using Decimal
    getcontext().prec = precision
    result = (Decimal(0.5)*(Decimal(1) + Decimal(5).sqrt()))
    return result


def main():
    gr = phi(1000)
    print(gr)


if __name__ == "__main__":
    main()