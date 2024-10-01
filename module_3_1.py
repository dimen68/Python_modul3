# Счётчик вызовов
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    list_to_search = (len(string), string.upper(), string.lower())
    print(list_to_search)
    return list_to_search

def is_contains(string, list_to_search):
    count_calls()
    condition = string.lower() in list_to_search
    print(condition)
    return condition


calls = 0
while calls < 19:
    string = input('Введите строку: ')
    list_to_search = string_info(string)
    is_contains(string, list_to_search)
    print(calls)
print(f'Программа завершена.\nФункции вызывались {calls} раз.')

