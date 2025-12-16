# Copy here code of line function from previous exercise
def line(num, string):
    if not string:
        print("*" * num)
    else:
        print(string[0] * num)


def triangle(size):
    counter = 0
    while counter <= size:
        line(counter, "#")
        counter += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)

