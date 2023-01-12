import time


def walk_collatz(n: int):
    while True:
        yield n
        if -1 <= n <= 1:
            break
        n *= 3 + 1 if n % 2 else n // 2


def main():
    start = time.time()
    for n in walk_collatz(11):
        print(n)
    end = time.time()
    print(f"{end-start}s")


if __name__ == "__main__":
    main()
