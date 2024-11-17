print('Эта программа сравнивает между собой значения введённых чисел с помощью условной конструкции if.')
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
print('Количество одинаковых чисел среди введённых равно:')
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)