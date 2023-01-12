def brainfuck(commands: str, num_cells=30_000):
    cells = bytearray(num_cells)
    d_ptr, i_ptr = 0, 0
    
    start_indices = []
    skipping = False

    while i_ptr < len(commands):
        if not skipping:
            match commands[i_ptr]:
                case ">":
                    d_ptr = (d_ptr + 1) % num_cells          # increment or wrap around if max index
                case "<":
                    d_ptr = (d_ptr - 1) % num_cells          # decrement or wrap around if 0
                case "+":
                    cells[d_ptr] = (cells[d_ptr] + 1) % 256  # increment current cell or wrap
                case "-":
                    cells[d_ptr] = (cells[d_ptr] - 1) % 256  # decrement current cell or wrap
                case ".":
                    yield cells[d_ptr]                       # output data in current cell
                case ",":
                    cells[d_ptr] = ord(input()[0])           # accept 1 ascii character
                case "[":
                    start_indices.append(i_ptr)
                    skipping = not cells[d_ptr]              # skip to command after next "]"
                case "]":
                    if cells[d_ptr]:
                        i_ptr = start_indices[-1]            # go to top of stack index
                    else:
                        start_indices.pop()                  # pop matching "[" index off stack

        if commands[i_ptr] == "]":
            skipping = False

        i_ptr += 1


def main():
    commands = """--[+++++++<---->>-->+>+>+<<<<]<.>++++[-<++++>>->--<<]>>-.>--..>+.<<<.<<-.>>+>->>.+++[.<]"""
    
    for out in brainfuck(commands):
        print(chr(out), end="")
    print("[END]")


if __name__ == "__main__":
    main()
