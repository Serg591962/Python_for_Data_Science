import pandas as pd
data = [["shanda", "smith", 43], ["rolly", "brocker", 23], ["molly", "stein", 78]]
index_labels = ['a', 'b', 'c']
dp = pd.DataFrame(data, index=index_labels)
print(dp)
dp.to_csv('my_participants.csv', index=False)
dp.to_csv('D:/wirt/project/my_dp.csv', index=False)
