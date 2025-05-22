def add_one(number): # 1Определяются функции
                        # 3.4: Вызов add_one(1):
    print("Adding 1")
    return number + 1   # 3.4.1. возвращается: 1 + 1 = 2

def do_wrapping(some_func):#1 Определяются функции
    print("wrapping function")# 2.1
    def wrapper(number): # 2.2: Определяется вложенная функция wrapper(number):
                            # 3.1 Вызов my_func(1)
        print("Before calling function")# 3.2:
        retval = some_func(number) # 3.3: Вызов some_func(number), то есть add_one(1).(some_func в wrapper — это add_one, переданная ранее в do_wrapping)
                                    # Фактически происходит retval = add_one(1) dызов add_one(1):
        print("After calling function") #3.5: 
        return retval # 3.6: wrapper возвращает значение 2 в my_func(1) :
    return wrapper # 2.3: Возвращается сама функция wrapper как объект:

my_func = do_wrapping(add_one)  # 2: Вызов do_wrapping(add_one)передаём объект функции add_one (без скобок!) как аргумент some_func.
                                # 2.3. 1: Возвращанная функция wrapper как объект присваивается переменной my_func
print(my_func(1))  # Шаг 3: Вызов my_func(1) и через нее вызов функции  wrapper передача ей аргумента 1 тк при my_func = do_wrapping(add_one)
                    # была Определяется вложенная функция wrapper(number):те my_func = wrapper  # wrapper «помнит» функцию add_one внутри
                    # 3.7: Выполняется print(...):


