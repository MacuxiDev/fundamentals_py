import requests
import pandas as pd
# Extraindo dados de uma API
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
if response.status_code == 200:
    dados = response.json()
    df_api = pd.DataFrame(dados)
    print(df_api.head())
else:
    print("Erro ao acessar a API:", response.status_code)