list = []
counter = 1
while True:
    print(f"The list is now {list}")
    to_do = input("a(d)d, (r)emove or e(x)it: ")
    if to_do == "d":
        list.append(counter)
        counter += 1
    elif to_do == "r":
        if not list:
            pass
        else:
            list.pop()
            counter -= 1
    elif to_do == "x":
        print("Bye!")
        break
