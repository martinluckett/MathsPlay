import time


def fibonacci(n):
    # generate fibonacci sequence to the nth term
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(b)
        a, b = b, a+b
    return sequence


def output_all(f):
    print("n", "Fibonacci Sequence")
    for i in range(0, len(f)):
        print(i+1, f[i])


def nth_term(f,n):
    try:
        result = f[n-1]
    except Exception as e:
        print("Error: {0}".format(e))
    else:
        return result


def main():
    start_time = time.time()
    f = fibonacci(100)
    run_time = str(time.time() - start_time)
    output_all(f)
    n = 99
    print("The {0}th term is {1}".format(n, nth_term(f, n)))
    print("run time: {0}".format(run_time))


if __name__ == "__main__":
    main()
