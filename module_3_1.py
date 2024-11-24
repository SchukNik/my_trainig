calls = 0

def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    string = input('Введите строку для получения информации о ней: ')
    return (len(string), string.upper(), string.lower())

def is_contains(string,  list_to_search):
    count_calls()
    new_list_to_search = [x.lower() for x in list_to_search]
    new_string = string.lower()
    for i in new_list_to_search:
        if new_string in new_list_to_search:
            return (True)
            break
        else:
            return (False)
            break

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)