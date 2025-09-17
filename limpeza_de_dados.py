import pandas as pd

df = pd.read_csv('c:/Users/lucas/Documents/py/dados.csv')

# Removendo linhas com valores nulos
df = df.dropna()
# Preenchendo valores nulos com a média da coluna
df['coluna'] = df['coluna'].fillna(df['coluna'].mean())
# Removendo linhas duplicadas
df = df.drop_duplicates()
# Substituindo valores inválidos
df['categoria'] = df['categoria'].replace({'inválido': 'desconhecido'})