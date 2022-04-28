import pandas as pd

data = pd.read_csv("bos2021ModC.csv", sep=";")

print(data)

#print(data.columns)

#print(data.indiv_id)

data.to_csv('writing_data.csv',index=False)