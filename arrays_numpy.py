import numpy as np

# Array unidimensional (vetor)
vetor = np.array([1, 2, 3, 4, 5])
print("Vetor:", vetor)
# Array bidimensional (matriz)
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print("Matriz:\n", matriz)
# Array com valores zeros ou uns
zeros = np.zeros(5)
uns = np.ones(5)
print("Zeros:", zeros)
print("Uns:", uns)
# Array com uma sequência de números
sequencia = np.arange(1, 11, 2) # De 1 a 10, pulando de 2 em 2
print("Sequência:", sequencia)

# Arrays para operações
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])
# Operações básicas
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)

# Dados de exemplo
dados = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# Estatísticas básicas
media = np.mean(dados)
mediana = np.median(dados)
desvio_padrao = np.std(dados)
soma_total = np.sum(dados)
minimo = np.min(dados)
maximo = np.max(dados)
print("Média:", media)
print("Mediana:", mediana)
print("Desvio Padrão:", desvio_padrao)
print("Soma:", soma_total)
print("Mínimo:", minimo)
print("Máximo:", maximo)

# Array de exemplo
vetor = np.array([10, 20, 30, 40, 50, 60])
# Acessando elementos
print("Primeiro elemento:", vetor[0])
print("Último elemento:", vetor[-1])
# Fatiamento
print("Elementos do índice 1 ao 4:", vetor[1:5])
print("Elementos até o índice 3:", vetor[:4])
print("Elementos do índice 3 em diante:", vetor[3:])