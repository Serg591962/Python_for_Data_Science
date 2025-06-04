import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
import os

# Готовим переменную заранее
tkdnd = None

# Пытаемся подключить поддержку перетаскивания
try:
    import tkinterdnd2 as tkdnd
    root = tkdnd.TkinterDnD.Tk()
except ImportError:
    root = tk.Tk()

# --- Функции ---
def convert_image():
    png_path = entry.get().strip().strip('"')
    if not os.path.isfile(png_path):
        messagebox.showerror("Ошибка", "Файл не найден!")
        return

    if not png_path.lower().endswith(".png"):
        messagebox.showerror("Ошибка", "Выберите PNG-файл.")
        return

    try:
        width = int(size_var.get().split("x")[0])
        height = int(size_var.get().split("x")[1])
    except:
        messagebox.showerror("Ошибка", "Некорректный размер.")
        return

    save_path = filedialog.asksaveasfilename(
        defaultextension=".ico",
        filetypes=[("ICO файлы", "*.ico")],
        title="Сохранить как...",
        initialfile="icon.ico"
    )

    if not save_path:
        return

    try:
        with Image.open(png_path) as img:
            img = img.convert("RGBA")
            img = img.resize((width, height))
            img.save(save_path, format="ICO")
        messagebox.showinfo("Успех", f"Иконка сохранена:\n{save_path}")
    except Exception as e:
        messagebox.showerror("Ошибка при конвертации", str(e))

def browse_file():
    file_path = filedialog.askopenfilename(
        title="Выберите PNG-файл",
        filetypes=[("PNG изображения", "*.png")]
    )
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

def on_drop(event):
    file_path = event.data.strip('{}')
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

# --- Интерфейс ---
root.title("PNG → ICO Конвертер")
root.geometry("460x230")
root.resizable(False, False)

tk.Label(root, text="1. Перетащите PNG-файл или выберите вручную:", font=("Arial", 10)).pack(pady=5)

entry = tk.Entry(root, width=60, justify='center')
entry.pack(pady=5)

# Если поддержка DND доступна — регистрируем drop
if tkdnd:
    entry.drop_target_register(tkdnd.DND_FILES)
    entry.dnd_bind('<<Drop>>', on_drop)

tk.Button(root, text="Выбрать PNG-файл", command=browse_file).pack(pady=5)

tk.Label(root, text="2. Выберите размер иконки:", font=("Arial", 10)).pack(pady=5)

size_var = tk.StringVar(value="64x64")
size_options = ["16x16", "32x32", "64x64", "128x128", "256x256"]
size_menu = ttk.Combobox(root, textvariable=size_var, values=size_options, state="readonly", width=10)
size_menu.pack(pady=2)

tk.Button(root, text="3. Конвертировать и сохранить", command=convert_image).pack(pady=10)

root.mainloop()
