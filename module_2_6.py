def passw(n):
    passw = ''
    i_list = []
    for i in range(1, n):
        i_list.append(i)
        for j in range(1, n):
            if i == j or j in i_list:
                continue
            if n % (i + j) == 0:
                passw = passw + str(i) + str(j)
    return passw


n = int(input('Введите число от 3 до 20: '))
while n not in range(3, 21):
    print('Введено значение вне диапазона')
    n = int(input('Введите число от 3 до 20: '))
result = passw(n)
print(f'Для числа {n} код: {result}')