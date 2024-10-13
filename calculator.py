# калькулятор
# импорт внутренний библиотеки
import tkinter as tk
# определение функций калькулятора:

#   функция приема введенных данных
def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

#   функция вывода данных
def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

# функция сложения
def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

# функция вычетания
def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

# функция деления
def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

# функция умножения
def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


# окно
window =tk.Tk()
window.title('Калькулятор')
window.geometry("400x400")
window.resizable(False, False)
# кнопки
button_add = tk.Button(window, text='+', width= 2, height=2, command=add)
button_add.place(x=100, y=200)
button_sub = tk.Button(window, text='-', width= 2, height=2, command=sub)
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, text='*', width= 2, height=2, command=mul)
button_mul.place(x=200, y=200)
button_div = tk.Button(window, text='/', width= 2, height=2, command=div)
button_div.place(x=250, y=200)
# поля ввода и вывода
number1_entry = tk.Entry(window, width=30)
number1_entry.place(x=100, y=75)
number2_entry = tk.Entry(window, width=30)
number2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=30)
answer_entry.place(x=100, y=275)
# далее
pass
pass
# автообновление окна
window.mainloop()