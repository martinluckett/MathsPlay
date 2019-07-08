# collatz.py
#
# If even, a is divided by 2
# If odd, a is multiplied by 3 and add 1 (3n + 1)
#
# The Collatz conjecture is:
# "...that no matter what value of n, the sequence will always reach 1"
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019


class Collatz:
    def __init__(self, initial_number):
        self.initial_number = initial_number
        self.name = "Collatz"
        self.seq = []
        self.counter = 0
        self.generate_sequence(initial_number)

    def generate_sequence(self, a):
        while a != 1:
            self.counter += 1
            self.seq.append(a)
            if a % 2 == 0:
                a = int(a / 2)
            else:
                a = a * 3 + 1
        self.seq.append(1)

    def test(self):
        coll_str = "For n = {n1}, the {name} sequence reaches 1 in {counter} steps\n\n" \
                   "{name} Sequence starting from {n1}:\n{seq}\n"
        print(coll_str.format(n1=self.initial_number, name=self.name, counter=self.counter, seq=self.seq))




