from PIL import Image
import os

def convert_png_to_ico():
    print("Конвертация PNG → ICO (64x64)")
    png_path = input("Введите путь к PNG-файлу: ").strip().strip('"')

    # Проверка существования файла
    if not os.path.isfile(png_path):
        print("❌ Файл не найден. Проверьте путь.")
        return

    # Получаем имя без расширения и создаём имя иконки
    base_name = os.path.splitext(os.path.basename(png_path))[0]
    ico_path = base_name + ".ico"
    icon_size = (64, 64)

    try:
        with Image.open(png_path) as img:
            img = img.convert("RGBA")
            img = img.resize(icon_size)
            img.save(ico_path, format="ICO")
        print(f"✅ Иконка успешно создана: {ico_path}")
    except Exception as e:
        print("❌ Ошибка при конвертации:", e)

# Запуск при выполнении из IDLE
if __name__ == "__main__":
    convert_png_to_ico()
    input("\nНажмите Enter для выхода...")
