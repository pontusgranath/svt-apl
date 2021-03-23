import pandas as pd

data = pd.read_csv('Data-Table 1.csv', sep=';')
data.set_index('Client ID (ns_vid)', inplace=True)

columns = list(data.columns)

print(columns)