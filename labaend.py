import requests
from bs4 import BeautifulSoup
import tkinter as tk #граф интерфейс
from tkinter import ttk
from datetime import datetime

def fetch_data():
    url = "https://gos.etpgpb.ru/44/catalog/procedure"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser") # парсинг

    data = []
    rows = soup.find_all("tr", {"id": lambda x: x and x.startswith("rowId-")})
    for row in rows:
        name = row.find("td", class_="row-procedure_name").get_text(strip=True)
        description = row.find("td", class_="row-type").get_text(strip=True)
        categories = row.find("td", class_="row-placer_region_id").get_text(strip=True)
        date = row.find("td", class_="row-publication_datetime").get_text(strip=True)
        price = row.find("td", class_="row-contract_start_price").get_text(strip=True).replace("RUB", "").strip()
        data.append({"name": name, "description": description, "categories": categories, "date": date, "price": price})
    return data


class App(tk.Tk):
    def __init__(self, data):
        super().__init__()
        self.title("Парсер данных")
        self.geometry("800x600")

        self.data = data
        self.filtered_data = data

        # Поля фильтрации
        self.search_name = tk.StringVar()
        self.category_filter = tk.StringVar()
        self.date_from = tk.StringVar()
        self.date_to = tk.StringVar()
        self.price_min = tk.StringVar()
        self.price_max = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        frame_filters = tk.Frame(self)
        frame_filters.pack(fill=tk.X, padx=5, pady=5)

        tk.Label(frame_filters, text="Название:").grid(row=0, column=0)
        tk.Entry(frame_filters, textvariable=self.search_name).grid(row=0, column=1)

        tk.Label(frame_filters, text="Категория:").grid(row=0, column=2)
        tk.Entry(frame_filters, textvariable=self.category_filter).grid(row=0, column=3)

        tk.Label(frame_filters, text="Дата с:").grid(row=1, column=0)
        tk.Entry(frame_filters, textvariable=self.date_from).grid(row=1, column=1)

        tk.Label(frame_filters, text="Дата по:").grid(row=1, column=2)
        tk.Entry(frame_filters, textvariable=self.date_to).grid(row=1, column=3)

        tk.Label(frame_filters, text="Цена от:").grid(row=2, column=0)
        tk.Entry(frame_filters, textvariable=self.price_min).grid(row=2, column=1)

        tk.Label(frame_filters, text="Цена до:").grid(row=2, column=2)
        tk.Entry(frame_filters, textvariable=self.price_max).grid(row=2, column=3)

        tk.Button(frame_filters, text="Применить фильтры", command=self.apply_filters).grid(row=3, column=0, columnspan=4)

        self.tree = ttk.Treeview(self, columns=("name", "description", "categories", "date", "price"), show="headings")
        self.tree.heading("name", text="Название")
        self.tree.heading("description", text="Описание")
        self.tree.heading("categories", text="Категории")
        self.tree.heading("date", text="Дата")
        self.tree.heading("price", text="Цена")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.populate_tree()

    def populate_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for item in self.filtered_data:
            self.tree.insert("", "end", values=(item["name"], item["description"], item["categories"], item["date"], item["price"]))

    def apply_filters(self):
        name_filter = self.search_name.get().lower()
        category_filter = self.category_filter.get().lower()
        date_from = self.date_from.get()
        date_to = self.date_to.get()
        price_min = self.price_min.get()
        price_max = self.price_max.get()

        self.filtered_data = self.data

        if name_filter:
            self.filtered_data = [item for item in self.filtered_data if name_filter in item["name"].lower()]

        if category_filter:
            self.filtered_data = [item for item in self.filtered_data if category_filter in item["categories"].lower()]

        if date_from:
            self.filtered_data = [item for item in self.filtered_data if datetime.strptime(item["date"].split()[0], "%d.%m.%Y") >= datetime.strptime(date_from, "%d.%m.%Y")]

        if date_to:
            self.filtered_data = [item for item in self.filtered_data if datetime.strptime(item["date"].split()[0], "%d.%m.%Y") <= datetime.strptime(date_to, "%d.%m.%Y")]

        if price_min:
            self.filtered_data = [item for item in self.filtered_data if float(item["price"].replace(" ", "").replace(",", ".")) >= float(price_min)]

        if price_max:
            self.filtered_data = [item for item in self.filtered_data if float(item["price"].replace(" ", "").replace(",", ".")) <= float(price_max)]

        self.populate_tree()


if __name__ == "__main__":
    data = fetch_data()
    app = App(data)
    app.mainloop()

