immutable_var = 1, 2.5, True, 'cat'
print(immutable_var)
# immutable_var[0] = 200 (ошибка, т.к. тип данных int внутри кортежа относится к неизменяемым, сам кортеж - тоже неизменямый тип данных, в отличии от списка)
mutable_list = [1, 2.5, True, 'cat']
mutable_list[0] = 200
print(mutable_list)