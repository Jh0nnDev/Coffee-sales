import pandas as pd
# lê o documento csv
df = pd.read_csv("data/coffee-sales.csv")

#transforma a coluna 'date' no formato de data
df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")

#  cria uma nova coluna que armazena apenas o mês
df['mes'] = df['date'].dt.month

# salva o documento
df.to_excel("data/coffee.xlsx")
print("O documento foi salvo com sucesso!")



#print(df.info()) - usar para saber as informações das colunas
#print(df.isnull().sum()) - usar para saber se existe valor nulo 