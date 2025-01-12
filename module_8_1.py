def add_everything_up(a, b):
    try:
        return round(a + b, 3)

    except TypeError:
        return str(a) + str(b)

    finally:
        print(f'Phyton не позволяет складывать числа и строки. Результат ниже '
                f'получился таким, потому что первый аргумент - это {type(a)}, '
                f'а второй - {type(b)}')

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
