from bs4 import BeautifulSoup
import requests
# Extraindo dados de uma página web
url = "https://moodle.ifsc.edu.br/course/view.php?id=3638"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
# Coletando os títulos dos artigos
titulos = [elemento.text for elemento in
soup.find_all("h2")]
print(titulos)