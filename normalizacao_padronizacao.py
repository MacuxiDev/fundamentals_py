import numpy as np
import pandas as pd

#A normalização e a padronização garantem que os dados estejam em escalas
#comparáveis, o que é essencial para modelos de Machine Learning.
#Normalização para o Intervalo [0, 1]:

df = pd.read_csv('c:/Users/lucas/Documents/py/dados.csv')

df['valor_normalizado'] = (df['valor'] - df['valor'].min()) 
(df['valor'].max() - df['valor'].min())

#Padronização com Média 0 e Desvio Padrão 1:
df['valor_padronizado'] = (df['valor'] - df['valor'].mean()) 
df['valor'].std()

# Convertendo uma coluna para o tipo numérico
df['idade'] = pd.to_numeric(df['idade'], errors='coerce')

# Convertendo uma coluna para o formato de data
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')

# Criando uma nova coluna baseada em condições
df['faixa_etaria'] = df['idade'].apply(lambda x: 'Adulto' if x >= 18 else
'Menor')

# Combinando colunas existentes
df['nome_completo'] = df['nome'] + ' ' + df['sobrenome']