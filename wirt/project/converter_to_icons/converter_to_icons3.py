import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
import os
import sys

# Поддержка перетаскивания (если доступен tkinterdnd2)
tkdnd = None
try:
    import tkinterdnd2 as tkdnd
    root = tkdnd.TkinterDnD.Tk()
except ImportError:
    root = tk.Tk()

# --- Функции ---
def check_and_prepare_file(file_path):
    file_path = file_path.strip().strip('"')
    if not os.path.isfile(file_path):
        messagebox.showerror("Ошибка", "Файл не найден!")
        return None

    ext = os.path.splitext(file_path)[1].lower()
    allowed = [".png", ".img", ".jpg", ".jpeg"]

    if ext not in allowed:
        messagebox.showerror("Ошибка", "Поддерживаются только PNG, IMG, JPG, JPEG.")
        return None

    if ext != ".png":
        answer = messagebox.askyesno("Конвертация", "Файл не PNG. Конвертировать в PNG?")
        if not answer:
            root.destroy()
            sys.exit()

        try:
            with Image.open(file_path) as img:
                new_path = os.path.splitext(file_path)[0] + "_converted.png"
                img.save(new_path, format="PNG")
                return new_path
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка конвертации в PNG:\n{e}")
            return None

    return file_path

def convert_image():
    file_path = entry.get().strip().strip('"')
    if not os.path.isfile(file_path):
        messagebox.showerror("Ошибка", "Файл не найден!")
        return

    try:
        width, height = map(int, size_var.get().split("x"))
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
        with Image.open(file_path) as img:
            img = img.convert("RGBA")
            img = img.resize((width, height))
            img.save(save_path, format="ICO")
        messagebox.showinfo("Успех", f"Иконка сохранена:\n{save_path}")
    except Exception as e:
        messagebox.showerror("Ошибка при сохранении", str(e))

def browse_file():
    file_path = filedialog.askopenfilename(
        title="Выберите изображение",
        filetypes=[("Изображения (PNG, JPG, IMG)", "*.png *.jpg *.jpeg *.img")]
    )
    if file_path:
        new_path = check_and_prepare_file(file_path)
        if new_path:
            entry.delete(0, tk.END)
            entry.insert(0, new_path)

def on_drop(event):
    file_path = event.data.strip('{}')
    if file_path:
        new_path = check_and_prepare_file(file_path)
        if new_path:
            entry.delete(0, tk.END)
            entry.insert(0, new_path)

# --- Интерфейс ---
root.title("Изображение → Иконка")
root.geometry("460x230")
root.resizable(False, False)

tk.Label(root, text="Выберите файл для конвертации.", font=("Arial", 10)).pack(pady=5)

entry = tk.Entry(root, width=60, justify='center')
entry.pack(pady=5)

# Поддержка DND
if tkdnd:
    entry.drop_target_register(tkdnd.DND_FILES)
    entry.dnd_bind('<<Drop>>', on_drop)

tk.Button(root, text="Выбрать файл", command=browse_file).pack(pady=5)

tk.Label(root, text="2. Выберите размер иконки:", font=("Arial", 10)).pack(pady=5)

size_var = tk.StringVar(value="64x64")
size_options = ["16x16", "32x32", "64x64", "128x128", "256x256"]
size_menu = ttk.Combobox(root, textvariable=size_var, values=size_options, state="readonly", width=10)
size_menu.pack(pady=2)

tk.Button(root, text="3. Конвертировать и сохранить", command=convert_image).pack(pady=10)

root.mainloop()
