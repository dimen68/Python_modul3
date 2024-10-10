# калькулятор
# импорт внутренний библиотеки
import tkinter as tk
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