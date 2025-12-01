def squared(string, size):
    row = 0
    lenght = len(string)
    while row < size:
        col = 0
        string_to_print = ""
        while col < size:
            char_to_add = string[(row * size + col) % lenght]
            string_to_print += char_to_add
            col += 1
        print(string_to_print)
        row += 1


if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)
