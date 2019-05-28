import time


def fibonacci(n):
    # generate fibonacci sequence to the nth term
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(b)
        a, b = b, a+b
    return sequence


def output(f):
    print("n", "Fibonacci Sequence")
    for i in range(0, len(f)):
        print(i+1, f[i])


def main():
    start_time = time.time()
    f = fibonacci(1000)
    output(f)
    print("run time: " + str(time.time() - start_time))


if __name__ == "__main__":
    main()