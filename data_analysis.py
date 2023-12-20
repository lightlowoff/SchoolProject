import tkinter as tk
from tkinter import ttk


class GradeTableApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Таблиця оцінок учнів")

        self.tree = ttk.Treeview(master, columns=("Прізвище", "Оцінка"), show="headings")
        self.tree.heading("Прізвище", text="Прізвище")
        self.tree.heading("Оцінка", text="Оцінка")
        self.tree.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        self.name_entry = ttk.Entry(master)
        self.name_entry.grid(row=1, column=0, pady=5, padx=5, sticky=tk.W)

        self.grade_entry = ttk.Entry(master)
        self.grade_entry.grid(row=1, column=1, pady=5, padx=5, sticky=tk.E)

        add_button = ttk.Button(master, text="Додати", command=self.add_to_table)
        add_button.grid(row=2, column=0, columnspan=2, pady=10)

    def add_to_table(self):
        name = self.name_entry.get()
        grade = self.grade_entry.get()

        if name and grade:
            self.tree.insert("", "end", values=(name, grade))
            self.name_entry.delete(0, tk.END)
            self.grade_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = GradeTableApp(root)
    root.mainloop()
