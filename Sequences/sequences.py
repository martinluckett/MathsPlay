# sequences.py


def sequence(n, first_term, second_term, multiplier_first_term=1, multiplier_second_term=1):
    # generate sequence to the (n)th term
    seq = []
    # Set the first two terms
    a, b = first_term, second_term

    # Set the multipliers for the terms (default = 1)
    c, d = multiplier_first_term, multiplier_second_term

    # Add the first term to the sequence result
    seq.append(a)

    # Generate the sequence by adding the two previous terms
    while len(seq) < n+1:
        seq.append(b)
        a, b = b, (c*a)+(d*b)

    # Return the sequence of n terms
    return seq


