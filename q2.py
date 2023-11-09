# Exercício 2: Média de uma Lista
# Escreva um programa que calcule a média dos
# elementos em uma lista de números inteiros.

lista = input("Digite numeros inteiros separados por virgula:  ").split(" ")
soma=0
media=0
for i in range(len(lista)):
    soma=soma+int(lista[i])
media = soma/len(lista)
print(f"A média de elementos é: {media}")
