import tkinter as tk

# Функція для обробки кнопок
def on_button_click(value):
    # Результат дії
    if value == '=':
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        # Оброблюємо помилки
        except Exception as e:
            entry_var.set("Error")
    # Стираємо значення
    elif value == 'C':
        entry_var.set('')
    # Додавання символів до поточного значення
    else:
        current_text = entry_var.get()
        new_text = current_text + value
        entry_var.set(new_text)

# Створення основного вікна
root = tk.Tk()
root.title("Калькулятор")

# Змінна для збереження введених користувачем значень
entry_var = tk.StringVar()

# Елемент Entry для введення чисел
entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 14), bd=10, insertwidth=4, width=14, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Додавання кнопок для цифр та операцій
buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Додавання кнопок до вікна
for (text, row, col) in buttons:
    btn = tk.Button(root, text=text, font=('Arial', 14), command=lambda t=text: on_button_click(t))
    btn.grid(row=row, column=col, sticky='nsew')

# Налаштування розміру кнопок
for i in range(1, 5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Запуск головного циклу
root.mainloop()
