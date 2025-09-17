import pandas as pd

# Série simples
serie = pd.Series([10, 20, 30, 40, 50])
print("Série:\n", serie)

# Criando um DataFrame a partir de um dicionário
dados = {
"Nome": ["Ana", "Bruno", "Carlos", "Diana"],
"Idade": [25, 30, 35, 28],
"Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]
}
df = pd.DataFrame(dados)
print("DataFrame:\n", df)

print(df["Nome"]) # Acessa a coluna Nome
print(df[["Nome", "Idade"]]) # Acessa múltiplas colunas

print(df.iloc[0]) # Acessa a primeira linha pelo índice numérico
print(df.loc[0]) # Acessa a primeira linha pelo índice do DataFrame

# Adicionando uma nova coluna
df["Salario"] = [3000, 4000, 5000, 3500]
print(df)
# Filtrando dados
df_filtrado = df[df["Idade"] < 30]
print(df_filtrado)
# Calculando estatísticas
media_idade = df["Idade"].mean()
print("Média de idade:", media_idade)

# Acessando uma célula específica
print(df.at[1, "Nome"])
# Acessando um subconjunto de linhas e colunas
print(df.iloc[1:3, 0:2]) # Linhas de 1 a 2, colunas de 0 a 1
print(df.loc[0:2, ["Nome", "Cidade"]]) # Linhas de 0 a 2, colunas específicas

# Verificando valores ausentes
print(df.isnull().sum())
# Removendo linhas com valores ausentes
df_limpo = df.dropna()
# Preenchendo valores ausentes
df_preenchido = df.fillna("Desconhecido")