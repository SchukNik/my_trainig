my_dict = {'a' : 1, 'b' : 2, 'c' : 3}
print(my_dict)
print(my_dict.get('a'), my_dict.get('d'))
my_dict.update({'d' : 4,
               'e' : 5})
del my_dict['b']
print(my_dict)

my_set = {1, 2.5, 'string', 1, 2.5, True, 'string'}
print(my_set)
my_set.update([13, 'example'])
my_set.remove(2.5)
print(my_set)
