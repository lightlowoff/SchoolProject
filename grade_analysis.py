import tkinter as tk
from tkinter import ttk


class GradeAnalyzer:
    def __init__(self, master):
        self.master = master
        self.master.title("Аналізатор оцінок учня")

        self.grades = []

        label = ttk.Label(master, text="Введіть оцінки учня (через кому):")
        label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        self.grades_entry = ttk.Entry(master)
        self.grades_entry.grid(row=0, column=1, padx=10, pady=5)

        analyze_button = ttk.Button(master, text="Аналізувати", command=self.analyze_grades)
        analyze_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.result_table = ttk.Treeview(master, columns=("Категорія", "Кількість"), show="headings")
        self.result_table.heading("Категорія", text="Категорія")
        self.result_table.heading("Кількість", text="Кількість")
        self.result_table.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def analyze_grades(self):
        grades_str = self.grades_entry.get()
        self.grades = [int(grade.strip()) for grade in grades_str.split(',')]

        for item in self.result_table.get_children():
            self.result_table.delete(item)

        if not self.grades:
            return

        max_grade = max(self.grades)
        min_grade = min(self.grades)
        avg_grade = sum(self.grades) / len(self.grades)

        grade_categories = {'Початковий': 0, 'Середній': 0, 'Достатній': 0, 'Високий': 0}

        for grade in self.grades:
            if grade >= 10:
                grade_categories['Високий'] += 1
            elif grade >= 8:
                grade_categories['Достатній'] += 1
            elif grade >= 6:
                grade_categories['Середній'] += 1
            else:
                grade_categories['Початковий'] += 1

        self.result_table.insert("", 0, values=["Найвищий бал", max_grade])
        self.result_table.insert("", 1, values=["Найнижчий бал", min_grade])
        self.result_table.insert("", 2, values=["Середній бал", avg_grade])

        for category, count in grade_categories.items():
            self.result_table.insert("", "end", values=[category, count])


if __name__ == "__main__":
    root = tk.Tk()
    app = GradeAnalyzer(root)
    root.mainloop()