# Exercício 5: Mesclar e Classificar Listas
# Peça ao usuário que insira duas listas de números
# inteiros separadas por espaços. Em seguida, seu
# programa deve mesclar as duas listas em uma única
# lista e, em seguida, classificar essa lista em ordem
# crescente. Finalmente, exiba a lista classificada.

lista1 = input("Digite numeros inteiros separados por espaço para lista 1: ").split(" ")
lista2 = input("Digite numeros inteiros separados por espaço para lista 2: ").split(" ")

lista3 = lista1+lista2
print(sorted(lista3))
