Установка виртуального  окружения для работы с pandas
**D:/Python/Python3_7_9** - установить питон
**cd /d/wirt**
**"/d/Python/Python3_13_4/python.exe" -m venv pandas_env** - создание виртуального окружения pandas_env привязанного к Python3_7_9
**source /d/wirt/pandas_env/Scripts/activate** - активировать виртуальное окружение
**python -m pip install --upgrade pip setuptools wheel** - обновить pip, setuptools и wheel
**pip install pandas** - установка pandas
**DataFrame** - это основная структура данных в библиотеке Pandas, аналог таблицы (как в Excel или базе данных), построенная на основе массива NumPy.
 Состоит из:
- Строк (имеют индекс)
- Столбцов (каждый — объект pandas.Series)
Может содержать разные типы данных в разных столбцах (в отличие от массива NumPy)