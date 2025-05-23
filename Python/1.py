# Шаг 1. Определяется декоратор — это обычная функция, принимающая другую функцию (func)
def decorator(func):  # func будет ссылкой на multiply
    # Шаг 5. Внутри создаётся wrapper — новая функция-обёртка, принимающая любые аргументы
    def wrapper(*args, **kwargs):
        print("Начало вычислений")  # Печатается перед вызовом оригинальной multiply
        result = func(*args, **kwargs)  # Шаг 7. Вызывается multiply(a, b) с переданными аргументами
        print("Конец вычислений")  # Печатается после выполнения multiply
        return result  # Шаг 8. Возвращается результат multiply
    return wrapper  # Шаг 6. decorator возвращает wrapper

# Шаг 2. Определяется функция multiply с двумя аргументами
# @decorator автоматически вызывает: multiply = decorator(multiply)
@decorator
def multiply(a, b):
    print(f"Перемножаем {a} * {b}")  # Шаг 7. Печатается в момент вызова multiply
    return a * b  # Возвращает результат умножения

# Шаг 3. multiply теперь указывает на wrapper (а не на оригинальную multiply)
# Вызовем multiply(3, 5), на самом деле будет вызван wrapper(3, 5)
res = multiply(3, 5)  # Шаг 4. Вызывается wrapper с аргументами (3, 5)

# Шаг 9. Выводим результат, который вернул wrapper (он же результат multiply)
print(f"Результат: {res}")

