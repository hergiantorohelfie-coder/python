import tkinter as tk
import os

root = tk.Tk()
root.title("Konverter Suhu")
root.geometry("300x180")

base_dir = os.path.dirname(__file__)
icon_path = os.path.join(base_dir, "calc.ico")

if os.path.exists(icon_path):
    root.iconbitmap(icon_path)

def konversi():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        label_hasil.config(text=f"Hasil: {fahrenheit:.1f} °F", fg="green")
    except ValueError:
        label_hasil.config(text="Masukkan angka yang valid!", fg="red")

tk.Label(root, text="Suhu (Celsius):", font=('Arial', 11)).pack(pady=(15, 5))

entry_celsius = tk.Entry(root, font=('Arial', 12), justify="center")
entry_celsius.pack(pady=5)

btn_hitung = tk.Button(root, text="Konversi ke Fahrenheit", command=konversi, font=('Arial', 10, 'bold'))
btn_hitung.pack(pady=10)

label_hasil = tk.Label(root, text="Hasil: -", font=('Arial', 11, 'bold'))

label_hasil.pack(pady=5)

root.mainloop()