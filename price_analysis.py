import tkinter as tk
from tkinter import ttk


class PriceAnalyzerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Аналізатор цін")

        self.master.geometry("400x300")

        self.price_text = tk.Text(master, height=10, width=40)
        self.price_text.grid(row=0, column=0, padx=10, pady=10)

        analyze_button = ttk.Button(master, text="Аналізувати", command=self.analyze_prices)
        analyze_button.grid(row=1, column=0, pady=10)

        self.min_price_label = ttk.Label(master, text="Мінімальна ціна:")
        self.min_price_label.grid(row=2, column=0, pady=5)

        self.max_price_label = ttk.Label(master, text="Максимальна ціна:")
        self.max_price_label.grid(row=3, column=0, pady=5)

        self.avg_price_label = ttk.Label(master, text="Середня ціна:")
        self.avg_price_label.grid(row=4, column=0, pady=5)

    def analyze_prices(self):
        prices_str = self.price_text.get("1.0", "end-1c")
        prices_list = [float(price) for price in prices_str.splitlines() if price]

        if prices_list:
            min_price = min(prices_list)
            max_price = max(prices_list)
            avg_price = sum(prices_list) / len(prices_list)

            self.min_price_label.config(text=f"Мінімальна ціна: {min_price:.2f}")
            self.max_price_label.config(text=f"Максимальна ціна: {max_price:.2f}")
            self.avg_price_label.config(text=f"Середня ціна: {avg_price:.2f}")
        else:
            self.min_price_label.config(text="Мінімальна ціна: -")
            self.max_price_label.config(text="Максимальна ціна: -")
            self.avg_price_label.config(text="Середня ціна: -")


if __name__ == "__main__":
    root = tk.Tk()
    app = PriceAnalyzerApp(root)
    root.mainloop()
