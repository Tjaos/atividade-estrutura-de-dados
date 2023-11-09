# Exercício 3: Maior e Menor Elemento
# Escreva um programa que encontre o maior e o menor
# elemento em uma lista de números inteiros.

lista = input("Digite numeros inteiros separados por espaço: ").split(" ")

maior = 0
menor = min(lista)
for i in range(len(lista)):
    if int(lista[i]) > maior:
        maior = int(lista[i])
    
print(f"O maior numero da lista: {maior}")
print(f"O Menor numero da lista: {menor}")

