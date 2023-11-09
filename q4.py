# Exercício 4: Filtro de Elementos
# Escreva um programa que crie uma nova lista contendo
# apenas os elementos pares de uma lista de números
# inteiros.
lista = input("Digite numeros inteiros separados por espaço: ").split(" ")
pares = []
for i in range(len(lista)):
    if int(lista[i])%2 == 0:
        pares.append(lista[i]) 
    
print(pares)