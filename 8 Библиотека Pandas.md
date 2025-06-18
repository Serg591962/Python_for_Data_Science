Установка виртуального  окружения для работы с pandas
**D:/Python/Python3_13_3** - установить питон
**cd /d/wirt**
**"/d/Python/Python3_13_3/python.exe" -m venv pandas_env** - создание виртуального окружения pandas_env привязанного к Python3_13_3
**source /d/wirt/pandas_env/Scripts/activate** - активировать виртуальное окружение
**python -m pip install --upgrade pip setuptools wheel** - обновить pip, setuptools и wheel
**pip install pandas** - установка pandas
**DataFrame** - это основная структура данных в библиотеке Pandas, аналог таблицы (как в Excel или базе данных), 
DataFrame — это ключевая структура данных в библиотеке **Pandas**, которая используется в анализе данных, построенная на основе массива NumPy. Она представляет собой таблицу с метками строк и столбцов, очень похожую на Excel-таблицу, но с мощными возможностями программной обработки.
 - **DataFrame** — это двумерная таблица данных с подписями (метками) строк (имеют индекс) и столбцов, каждый — объект pandas.Series). Основан на **NumPy**, но может содержать **разные типы данных** в разных столбцах.
- **Series** — это один столбец таблицы, по сути, **одномерный массив с подписями**.
###### **Создание DataFrame**
###### **Пустой DataFrame:**
import pandas as pd
df = pd.DataFrame()
print(df) =>      Empty DataFrame
			Columns: []
			Index: []
###### **Из словаря:**
import pandas as pd
`first_names = ['shanda', 'rolly', 'molly'] #- создается список`
`ages = [43, 23, 78]`
`data = {'first': first_names, 'ages': ages} #- из списков создается словарь`
`dp = pd.DataFrame(data) #- создание DataFrame, таблица (похожую на Excel)`
print(dp) =>           first     ages
			0  shanda    43
			1   rolly       23
			2   molly     78
###### **Из списка списков:**
import pandas as pd
`data = [["shanda", "smith", 43], ["rolly", "brocker", 23], ["molly", "stein", 78]]`
dp = pd.DataFrame(data)
print(dp) =>             0            1            2
			0   shanda    smith       43
			1   rolly        brocker    23
			2   molly      stein         78
**задавая имена столбцов:**
import pandas as pd
`data = [["shanda", "smith", 43], ["rolly", "brocker", 23], ["molly", "stein", 78]]`
`column_names = ['first', 'last', 'ages']`
dp = pd.DataFrame(data, columns=column_names)
print(dp) =>            first        last          ages
			0   shanda    smith        43
			1   rolly         brocker    23
			2   molly       stein         78
**задавая индексы:**
import pandas as pd
`data = [["shanda", "smith", 43], ["rolly", "brocker", 23], ["molly", "stein", 78]]`
`index_labels = ['a', 'b', 'c']`
dp = pd.DataFrame(data, index=index_labels)
print(dp) =>             0          1            2
			a  shanda    smith     43
			b   rolly       brocker  23
			c   molly     stein       78
**загрузка из файлов**
dp.to_csv('my_dp.csv', index=False) => сохранение DataFrame dp в CSV-файл my_dp.csv в текущей рабочей папке не сохраняя индекс .
dp.to_csv('D:/wirt/project/my_dp.csv', index=False) => сохранение DataFrame dp в CSV-файл my_dp.csv по адресу D:\wirt\project
dp = pd.read_csv('my_dp.csv') => загрузка из текущей папки
dp = pd.read_csv('D:/wirt/project/pandas/my_dp.csv')=> загрузка по адресу
**статистика**
print(dp.head())       # первые 5 строк
print(dp.tail(3))      # последние 3 строки
print(dp.shape)        # количество строк, количество столбцов
print(dp.columns)      # => Index(['0', '1', '2'], dtype='object') -  имена столбцов
print(dp.index)        # => RangeIndex(start=0, stop=3, step=1) - индексация строк начинается с 0 (start=0) и идет до 3 (не включая 3) (stop=3)  с шагом индексации — 1 (step=1). То есть строки в датафрейме имеют индексы: 0, 1, 2
print(dp.describe())   # сводная статистика для числовых столбцов
			2
	count    3.000000   - количество непустых (ненулевых) значений
	mean    48.000000 - среднее арифметическое
	std        27.838822 - стандартное отклонение
	min       23.000000 - минимальное значение
	25%      33.000000 - первый квартиль (Q1), 25% значений меньше или равны этому числу
	50%      43.000000 - медиана (Q2), среднее значение: ровно посередине между наименьшим и наибольшим, если отсортировать.
	75%     60.500000  - третий квартиль (Q3), 75% значений меньше или равны этому числу.
	max     78.000000  - максимальное значение
**доступ к данным**
по имени столбца:
`print(dp['first'])` =>       0    shanda
						1     rolly
						2     molly
						Name: first, dtype: object
по строкам:
`dp[3:6]` - возврат 3 - 5 строк
`dp.iloc[0]`      # первая строка (по позиции)
`dp.loc['a']`     # строка по метке индекса
несколько столбцов:
`dp[['first', 'ages']]`
**управление DataFrame**
добавление нового столбца данных строки
`ages1 = [403, 203, 708]` - строка
`dp['ages12'] = ages1` - добавление нового столбца с названием 'ages12' состоящего из данных строки ages1`
добавление пустого столбца
dp['email'] = None
dp['email'] = ''
добавление нового столбца состоящего из двух столбцов датафрейма разного типа:
dp['full_name'] = dp['first'] + ' ' + dp['ages'].astype(str)
dp['ages'].astype(str) - числовые значения преобразовываться в строковые
добавление нового столбца состоящего из суммы значений двух столбцов датафрейма
dp['full'] = dp['ages'] + dp['ages12']
удаление столбца
dp2 = dp.drop(columns=['age']) - удаление столбца и создание нового датафрейма
dp.drop(columns=['ages'], inplace=True) - удаление столбца в исходном датафрейме
переименование столбца
dp.rename(columns={'first': 'First Name'}, inplace=True) - переименование столбца в исходном датафрейме
dp2 = dp.rename(columns={'first': 'First Name'}) - переименование столбца и создание нового датафрейма
dp.rename(columns={'first': 'First Name', 'age': 'Age'}, inplace=True) - переименовать несколько столбцов сразу
**управление данными**
Фильтрация:
`print([dp['ages'] > 40])` =>  `[0     True`
							1    False
							2     True
							Name: ages, dtype: bool]
`print(dp[dp['ages'] >= 40])` => выведет часть датафрейма соответствующую условию
Сортировка:
print(dp.sort_values(by='ages')) - сортировка по возрастающей
print(dp.sort_values(by='ages', ascending=False)) - обратная сортировка
Заполнение пропущенных значений:
dp.fillna(0)
Удаление строк с пропущенными значениями:
dp.dropna()
###### **Управление данными**
изменение данные
`dp.loc['h', 'ages']` = 5 => значение ячейки строки 'h и столбца 'ages' заменяется на 5
`dp.iloc[3, 'ages'] = 78` => значение ячейки строки 3 и столбца 'ages' заменяется на 78
`dp['Age'] -= 1`  # уменьшаем значение все ячеек столбца 'Age' на 1
`dp*= 2  # умножаем значение всех ячеек датефрейма на 2
dp.replace('Maul', 'Smiley', inplace=True) - в текущей таблице ячейки со значением 'Maul' заменяются на  'Smiley'
dp = dp.replace('Maul', 'Smiley') - возвращает копию таблицы с заменой и сохраняет её обратно в переменную dp
dp2 = dp.replace('Maul', 'Smiley') - возвращает копию таблицы с заменой и сохраняет её в переменную dp2