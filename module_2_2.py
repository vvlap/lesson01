first=input('Введите первое значение: ')
second=input('Введите второе значение: ')
third=input('Введите третье значение: ')

if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)