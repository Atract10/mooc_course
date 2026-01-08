list = [1, 2, 3, 4, 5]
index = int(input("Index: "))
while index != -1:
    new_value = int(input("New value: "))
    list[index] = new_value
    print(list)
    index = int(input("Index: "))

