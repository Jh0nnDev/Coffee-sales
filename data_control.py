import pandas as pd
# lê o documento csv
df = pd.read_csv("data/coffee-sales.csv")

print(df.info()) #- usar para saber as informações das colunas
print(df.isnull().sum()) #- usar para saber se existe valor nulo 