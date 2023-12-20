import tkinter as tk
from tkinter import ttk
from math import sqrt


class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Квадрат та Корінь")

        self.number_entry = ttk.Entry(master)
        self.number_entry.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        square_button = ttk.Button(master, text="Квадрат", command=self.calculate_square)
        square_button.grid(row=1, column=0, pady=5, padx=5, sticky=tk.W)

        sqrt_button = ttk.Button(master, text="Корінь", command=self.calculate_square_root)
        sqrt_button.grid(row=1, column=1, pady=5, padx=5, sticky=tk.E)

        self.square_label = ttk.Label(master, text="Квадрат:")
        self.square_label.grid(row=2, column=0, pady=5, padx=5, sticky=tk.W)

        self.sqrt_label = ttk.Label(master, text="Корінь:")
        self.sqrt_label.grid(row=2, column=1, pady=5, padx=5, sticky=tk.E)

    def calculate_square(self):
        try:
            number = float(self.number_entry.get())
            result_square = number ** 2
            self.square_label.config(text=f"Квадрат: {result_square:.2f}")
        except ValueError:
            self.square_label.config(text="Введіть дійсне число")

    def calculate_square_root(self):
        try:
            number = float(self.number_entry.get())
            if number >= 0:
                result_sqrt = sqrt(number)
                self.sqrt_label.config(text=f"Корінь: {result_sqrt:.2f}")
            else:
                self.sqrt_label.config(text="Введіть додатне число")
        except ValueError:
            self.sqrt_label.config(text="Введіть дійсне число")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()