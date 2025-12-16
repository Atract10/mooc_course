# Write your solution here
def spruce(size):
    print("a spruce!")
    counter = 0
    spaces_amount = size - 1
    string_to_print = ""
    while counter < size:
        print(spaces_amount * " " + "*" + string_to_print)
        string_to_print += "**"
        counter += 1
        spaces_amount -= 1
    print((size - 1) * " " + "*")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)

