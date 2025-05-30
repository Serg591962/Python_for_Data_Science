from scipy import misc
import matplotlib.pyplot as plt

print("Старт скрипта")

# Цветное изображение (ёж на траве)
face = misc.face()
print(face)

plt.imshow(face)
plt.title("Цветное изображение: scipy.misc.face()")
plt.axis('off')  # Отключаем оси
plt.show()

# Чёрно-белое изображение (текстура гор)
ascent = misc.ascent()
print(ascent)
plt.imshow(ascent, cmap='gray')
plt.title("Чёрно-белое изображение: scipy.misc.ascent()")
plt.axis('off')  # Отключаем оси
plt.show()

