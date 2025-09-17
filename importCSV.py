import pandas as pd 

df = pd.read_csv('c:/Users/lucas/Documents/py/dados.csv')

print(df.head())

# Salvando um DataFrame em um arquivo CSV
df.to_csv("c:/Users/lucas/Documents/py/dados.csv", index=False)
print(df.head())
# Exibindo informações gerais
print(df.info())
# Descrevendo as estatísticas básicas
print(df.describe())