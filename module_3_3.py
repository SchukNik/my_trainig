def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(1, 'Жук', False)
print_params('Паук', True, 46)
print_params(19, 19)
print_params('19')
print_params(b = 25)
print_params(c = [1,2,3])
print()

values_list = ['Строка', 7, False]
values_dict = {'a': False, 'b': 'Текст', 'c': 33}
print_params(*values_list)
print_params(**values_dict)
print()

values_list_2 = ['Одиннадцать', 11]
print_params(*values_list_2, 42)