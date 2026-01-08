values_list = []
how_many_times = int(input("How many items: "))
counter = 0
while counter < how_many_times:
    value_to_add = int(input(f"Item {counter + 1}: "))
    values_list.append(value_to_add)
    counter += 1

print(values_list)

