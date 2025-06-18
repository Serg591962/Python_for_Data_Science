import pandas as pd

first_names = ['shanda', 'rolly', 'molly'] #- создается список`
ages = [43, 33, 78]
data = {'first': first_names, 'ages': ages} #- из списков создается словарь`
dp = pd.DataFrame(data) #- создание DataFrame, таблица (похожую на Excel)`
print(dp)


dp.loc[0, 'first'] = 'Paul'
print(dp)
dp.loc[0, 'first'] = 'Maul'
print(dp)
dp2 = dp.replace('Maul', 'Smiley')
print(dp2)
dp.replace(r'(s)([a-z]+)', r'S\2', regex=True)
