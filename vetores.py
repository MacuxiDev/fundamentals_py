vetor =[1, 3, 5, 7, 9]

print(vetor[0])  # Acessa o primeiro elemento
print(vetor[-1])  # Acessa o ultimo elemento

for elemento in vetor:
    print(elemento, end=" ") # Imprime todos os elementos na mesma linha

# Soma dos elementos
soma = sum(vetor)
print("Soma dos elementos:", soma)

# Tamanho do vetor
tamanho = len(vetor)
print("Tamanho do vetor:", tamanho)

# Média dos elementos
media = soma / tamanho
print("Média dos elementos:", media)