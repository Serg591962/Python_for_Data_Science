def add_one(number): # 1Определяются функции
    print("Adding 1")
    return number + 1

def do_wrapping(some_func):#1 Определяются функции
    print("wrapping function")# 2.1
    def wrapper(number): # 2.2: Определяется вложенная функция wrapper(number):
        print("Before calling function")# 3.1:
        retval = some_func(number) # 3.2: Вызов some_func(number), то есть add_one(1)
        print("After calling function")
        return retval
    return wrapper # 2.3: Возвращается сама функция wrapper как объект:

my_func = do_wrapping(add_one)  # 2: Вызов do_wrapping(add_one)передаём объект функции add_one (без скобок!) как аргумент some_func.
                                # 2.3. 1: Возвращанная функция wrapper как объект присваивается переменной my_func
print(my_func(1))  # Шаг 3: Вызов my_func(1) и через нее вызов функции  wrapper передача ей аргумента 1


