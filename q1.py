# Exercício 1: Contagem de Elementos
# Escreva um programa que conte o número de
# ocorrências de um elemento específico em uma lista.

elementos = input("Digite quaisquer elementos separados por virgula: ").split(",")

print(elementos)

contar = input("Qual elemento contar?  ")

contador=0
for i in range(len(elementos)):
    if contar== elementos[i]:
        contador=contador+1
print(contador)