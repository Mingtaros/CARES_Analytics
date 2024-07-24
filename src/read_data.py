import pandas as pd

cares = pd.read_excel("data/CARES_data.xlsx", "Sheet1")
print(cares.shape)
