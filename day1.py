def get_majority(numbers: list[int]) -> int:
    """Day 1: Find number occurring more than half the time in list."""
    counts = {}
    mid = len(numbers) // 2
    
    for i in numbers:
        try:
            counts[i] += 1
        except KeyError:
            counts[i] = 1
        if counts[i] > mid:
            return i


def main():
    array = [1,0]
    print(get_majority(array))


if __name__ == "__main__":
    main()
