import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def convert_image(png_path):
    if not os.path.isfile(png_path):
        messagebox.showerror("Ошибка", "Файл не найден!")
        return

    if not png_path.lower().endswith(".png"):
        messagebox.showerror("Ошибка", "Пожалуйста, выберите PNG-файл.")
        return

    base_name = os.path.splitext(os.path.basename(png_path))[0]
    ico_path = os.path.join(os.path.dirname(png_path), base_name + ".ico")
    icon_size = (64, 64)

    try:
        with Image.open(png_path) as img:
            img = img.convert("RGBA")
            img = img.resize(icon_size)
            img.save(ico_path, format="ICO")
        messagebox.showinfo("Успех", f"Иконка создана:\n{ico_path}")
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
        convert_image(file_path)

def on_drop(event):
    # Получение перетаскиваемого пути
    file_path = event.data.strip('{}')  # Убираем фигурные скобки, если есть
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)
        convert_image(file_path)

# --- Интерфейс ---
root = tk.Tk()
root.title("PNG → ICO Конвертер")
root.geometry("400x150")
root.resizable(False, False)

label = tk.Label(root, text="Перетащите PNG-файл сюда или выберите вручную", font=("Arial", 10))
label.pack(pady=10)

entry = tk.Entry(root, width=50, justify='center')
entry.pack(pady=5)

browse_button = tk.Button(root, text="Выбрать PNG-файл", command=browse_file)
browse_button.pack(pady=5)

# Поддержка перетаскивания (только Windows с `tkdnd`)
try:
    import tkinterdnd2 as tkdnd
    root.destroy()
    
    class App(tkdnd.TkinterDnD.Tk):
        def __init__(self):
            super().__init__()
            self.title("PNG → ICO Конвертер")
            self.geometry("400x150")
            self.resizable(False, False)

            tk.Label(self, text="Перетащите PNG-файл сюда или выберите вручную", font=("Arial", 10)).pack(pady=10)

            self.entry = tk.Entry(self, width=50, justify='center')
            self.entry.pack(pady=5)

            tk.Button(self, text="Выбрать PNG-файл", command=browse_file).pack(pady=5)

            self.entry.drop_target_register(tkdnd.DND_FILES)
            self.entry.dnd_bind('<<Drop>>', lambda e: on_drop(e))

    app = App()
    entry = app.entry
    app.mainloop()

except ImportError:
    root.mainloop()
