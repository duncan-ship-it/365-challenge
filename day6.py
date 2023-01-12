opens = {
    ')': '(',
    ']': '[',
    '}': '{',
}


def valid_brackets(brackets: str) -> bool:
    starts = [None]
    
    for b in brackets:         
        if not opens.get(b):
            starts.append(b)
        elif opens[b] != starts.pop():
            return False
    return starts == [None]


def main():
    brackets = "[({})]"
    print(valid_brackets(brackets))
    
    
if __name__ == "__main__":
    main()
