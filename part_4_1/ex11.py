# Write your solution here
def find_word(str, what_word):
    index = 0
    word = ""
    counter = 0
    while index < len(str):
        if str[index] == " ":
            counter += 1
            if counter == what_word:
                break
            word = ""
        else:
            word += str[index]
        index += 1
    return word


def first_word(sentence):
    return find_word(sentence, 1)


def second_word(sentence):
    return find_word(sentence, 2)


def last_word(sentence):
    return find_word(sentence, 0)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))

