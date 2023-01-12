from math import log10, floor


def is_palindrome(num: int) -> bool:
    divisor = 1
    mirrored = 0
    
    while divisor <= num:
        factor, rem = divmod(num, divisor)
        print(factor, rem)
        mirrored += factor
        divisor *= 10
    
    return num == mirrored


def main():
    num = 123
    print(is_palindrome(num))


if __name__ == "__main__":
    main()
