import tkinter as tk
from tkinter import ttk


class TemperatureAnalyzer:
    def __init__(self, master):
        self.master = master
        self.master.title("Аналізатор температури")

        self.temperatures = []

        self.temperature_entries = []
        for i in range(12):
            label_text = f"Температура за місяць {i+1}:"
            label = ttk.Label(master, text=label_text)
            label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)

            entry = ttk.Entry(master)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.temperature_entries.append(entry)

        analyze_button = ttk.Button(master, text="Аналізувати", command=self.analyze_temperatures)
        analyze_button.grid(row=12, column=0, columnspan=2, pady=10)

        self.result_table = ttk.Treeview(master, columns=("Місяць", "Температура"), show="headings")
        self.result_table.heading("Місяць", text="Місяць")
        self.result_table.heading("Температура", text="Температура")
        self.result_table.grid(row=13, column=0, columnspan=2, padx=10, pady=10)

    def analyze_temperatures(self):
        self.temperatures = [float(entry.get()) for entry in self.temperature_entries]

        max_temp = max(self.temperatures)
        min_temp = min(self.temperatures)
        avg_temp = sum(self.temperatures) / len(self.temperatures)

        categories = ["Мороз", "Приморозок", "Помірна", "Жара"]
        count_temps = [0, 0, 0, 0]

        for temp in self.temperatures:
            if temp < 0:
                count_temps[0] += 1
            elif temp == 0:
                count_temps[1] += 1
            elif 0 < temp <= 20:
                count_temps[2] += 1
            else:
                count_temps[3] += 1

        for item in self.result_table.get_children():
            self.result_table.delete(item)

        self.result_table.insert("", 0, values=["Найбільше", max_temp])
        self.result_table.insert("", 1, values=["Найменше", min_temp])
        self.result_table.insert("", 2, values=["Середнє", avg_temp])
        self.result_table.insert("", 3, values=["Місяці з морозом", count_temps[0]])
        self.result_table.insert("", 4, values=["Місяці з приморозком", count_temps[1]])
        self.result_table.insert("", 5, values=["Місяці з помірною температурою", count_temps[2]])
        self.result_table.insert("", 6, values=["Місяці з жарою", count_temps[3]])


if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureAnalyzer(root)
    root.mainloop()