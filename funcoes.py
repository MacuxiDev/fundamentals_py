#funcao simples

def saudacao(nome):
    print(f"Oi, Programador {nome} :)")

saudacao("Lucas")

# funcao com retorno
def soma(a, b):
    return a + b

resultado = soma(1, 1)

print(f"Total soma: {resultado}")

#funcao com parametros opcinais

def apresentar(nome, idade=18):
    print(f"Nome: {nome} Idade: {idade}")

apresentar("Lucas", 20)
apresentar("Dani")  # idade padrão 18

# args e kwargs 

#Soma uma quantidade variável de números
def soma_total(*numeros):
    return sum(numeros)

print(soma_total(1, 1, 1, 1, 1))

#Exibe informações de forma flexível
def exibir_informacoes(**info):
    for chave, valor in info.items():
        print(f"{chave}: {valor}")

exibir_informacoes(nome="Ana", idade=25, cidade="São Paulo")