# Write your solution here
def greatest_number(num1, num2, num3):
    if num1 > num2:
        max_num = num1
    else:
        max_num = num2
    if max_num > num3:
        pass
    else:
        max_num = num3
    return max_num


# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)

