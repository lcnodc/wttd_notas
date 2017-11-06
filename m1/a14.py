#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""Listas são sequencias mutáveis.
- Métodos de listas: sort, append
- Listas podem armazenar qualquer tipo de objeto.
- Dentro da lista, ficarão somente as referências para os objetos.
- Nas listas, podemos utilizar aquelas sintaxes utilizadas em str.
- Alterar uma variável que possui uma cópia de uma referência a uma
    lista, alterará todas as variáveis que referenciam aquela lista.
-
"""


def main():

    # Declarando uma lista
    lista = [2, 7, 4,]
    print(lista)

    # Ordenando a lista
    lista.sort()
    # Retorna none, pq altera a lista.
    print(lista)

    # Verificando o tamanho da lista
    print(len(lista))

    # Copiando uma lista, porém estou copiando a referência da lista
    lista1 = lista

    # Add item na lista
    lista.append(10)

    # As duas lista apontam para a mesma referência
    print(lista, lista1)

    # Copiando uma lista, agora, copiando somente os valores
    lista2 = lista[:]

    # Add item na lista
    # Retorna none.
    lista.append(10)

    print(lista, lista1, lista2)

    # Lista com tipos mutáveis
    lista3 = [1, 2, 3, lista2,]

    # Assim, alterando a lista2, impactará na lista existente dentro de 3.
    lista2.append(12)

    # Da mesma forma, alterando a lista existente dentro de 3 alterará na 2.
    lista2.append(12)

    print(lista)
    print(lista1)
    print(lista2)
    print(lista3)

    # Copiar lista
    l = [1, 2, 3, 4,]
    k = l[:]

    # Testando se os id's são os mesmos.
    print(id(l) == id(k))

if __name__ == "__main__":
    main()
