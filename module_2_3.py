my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
while len(my_list) != 0:
    a = my_list.pop(0)
    if a == 0:
        continue
    elif a > 0:
        print(a)
    else:
        break



