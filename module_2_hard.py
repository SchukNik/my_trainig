n = int(input('Введите число из первой вставки: '))

for_pair_1 = list(range(1, n))
for_pair_2 = list(range(1, n))
result = ''

for i in for_pair_1:
    for j in for_pair_2:
        a = i
        b = j
        if a >= b:
            continue
        else:
            c = n % (a + b)
            if c == 0:
                result = result + str(a) + str(b)
print('Пароль для второй вставки:', result)