# sequences.py

error_str = "Error: {0}"
run_time_str = "{0} numbers run time: {1} seconds"
nth_term_str = "The {0}th term of the {1} numbers is {2}"
filename_str = "{0}_{1}.txt"


def sequence(n, first_term, second_term):
    # generate sequence to the (n)th term
    seq = []
    # Set the first two terms
    a, b = first_term, second_term
    seq.append(a)
    # Generate the sequence by adding the two previous terms
    while len(seq) < n+1:
        seq.append(b)
        a, b = b, a+b
    return seq


def output_all_to_screen(seq):
    print("n", "Sequence")
    for i in range(0, len(seq)):
        print("{0} {1}".format(i, seq[i]))


def output_all_to_file(seq, filename):
    try:
        with open(filename, "w") as file:
            for i in range(0, len(seq)):
                seq_str = "{0} {1}\n".format(i, seq[i])
                file.write(seq_str)
    except IOError as e:
        print(error_str.format(e))
    except TypeError as e:
        print(error_str.format(e))


def nth_term(seq, n):
    try:
        result = seq[n]
    except IndexError as e:
        print(error_str.format(e))
    else:
        return result
