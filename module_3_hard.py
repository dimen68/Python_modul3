# Задание "Раз, два, три, четыре, пять .... Это не всё?"
def calculate_structure_sum(data):
    global sum_
    for i in range(0, len(data)):
        if isinstance(data[i], list):
            a = data[i]
            calculate_structure_sum(a)
        elif isinstance(data[i], dict):
            b= list()
            b.extend(data[i].keys())
            b.extend(data[i].values())
            calculate_structure_sum(b)
        elif isinstance(data[i], tuple):
            c = list(data[i])
            calculate_structure_sum(c)
        elif isinstance(data[i], set):
            d = list(data[i])
            calculate_structure_sum(d)
        elif isinstance(data[i], str):
            sum_ += len(data[i])
        elif isinstance(data[i], int):
            sum_ += data[i]
        else: # None и т.д
            continue
    return sum_


sum_ = 0
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)