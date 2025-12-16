# Copy here code of line function from previous exercise and use it in your solution
def line(num, string):
    if not string:
        print("*" * num)
    else:
        print(string[0] * num)


def square(height, width, character):
    i = 0
    while i < height:
        line(width, character)
        i += 1


def triangle(width, character):
    counter = 0
    while counter <= width:
        line(counter, character)
        counter += 1


def shape(width, character1, height, character2):
    triangle(width, character1)
    square(height, width, character2)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "X", 3, "*")

