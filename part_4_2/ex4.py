words_list = []
counter = 0
while True:
    input_word = input("Word: ")
    if input_word not in words_list:
        counter += 1
        words_list.append(input_word)
    else:
        print(f"You typed in {counter} different words")
        break

