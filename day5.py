numerals = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}


def to_numeral(num: int) -> str:
    symbols = ""
    is_tens = True
    
    for i in reversed(numerals.keys()):
        factor, rem = divmod(num, i)
        
        if factor == 4:  # simplify 4 repeating numerals
            symbols += numerals[i] + numerals[i * 5]
            num -= i * 4
        else:
            symbols += numerals[i] * factor
            num = rem

        if rem + i // 10 >= i and is_tens:
            symbols += numerals[i//10] + numerals[i]
            num -= i - i // 10
        
        is_tens = not is_tens

    return symbols

    
def main():
    num = 1997
    print(to_numeral(num))


if __name__ == "__main__":
    main()
