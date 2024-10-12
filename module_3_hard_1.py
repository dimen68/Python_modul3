'''' Исправления по комментариям преподавателя:
Здравствуйте, задание выполнено верно, но достичь желаемого вами результата
можно используя распаковку списков через звездочку в аргументе функции,
перебору значений внутри data не по индексам ( for i in data:).
Если текущий элемент является одно из разновидностей массива,
то мы прибавляем к sum результат работы функции от массива,
только предварительно его нужно распаковать.
Почитайте про *args **kwargs
'''
def calculate_structure_sum(data):
    sum_ = 0
    for i in data:
        if isinstance(i, (list, tuple, set)):
            a = [*i]
            sum_ += calculate_structure_sum(a)
        elif isinstance(i, dict):
            b= [*i.items()]
            sum_ += calculate_structure_sum(b)
        elif isinstance(i, str):
            sum_ += len(i)
        elif isinstance(i, int):
            sum_ += i
        else: # None и т.д
            continue
    return sum_


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)