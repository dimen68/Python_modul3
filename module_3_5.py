# Рекурсивное умножение цифр
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(21111140203) # 2*1*1*1*1*1*4*2*3
print(result)

