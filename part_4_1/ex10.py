def same_chars(string, num1, num2):
    string_lenghts = len(string)
    if string_lenghts > num1 and string_lenghts > num2:
        char_1 = string[num1]
        char_2 = string[num2]
        if char_1 == char_2:
            return True
        else:
            return False
    else:
        return False
