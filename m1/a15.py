#!/usr/bin/env python
#-*- coding: utf-8 -*-


def main():
    """ Tuplas são sequências imutáveis.
    - Qualquer alteração nelas, novos objetos serão criados.
    - Tem poucos métodos
    - Também suportam armazenar qualquer tipo de objeto
    - Assim como em outras sequences, posso trabalhar com slices
    - Porém, nela não consigo copia-la utilizando o operador :
    - Os parenteses não criam as tuplas e sim as virgulas
    - Praticando...
    """

    # Declarando...
    t = (1, 2, 3,) # ou
    t = 1, 2, 3 # veja que não precisa dos parenteses

    print(t)
    print(type(t))

    # Cria uma tupla de um elemento
    # Lembrando que se a virgula nao for declarada, o retorno será str.
    t = ('luciano',)
    print(t)
    print(type(t))

    # Cria uma tupla com 7 elementos str
    t = tuple('luciano')
    print(t)
    print(type(t))

    print(t[1])
    print(type(t[1]))

    # Copiando uma tupla
    t1 =  t[:]
    print(t, t1)

    # Verificando a referência de cada var.
    print(id(t), id(t1))

    # Criando tuplas sem parenteses
    t2 = 5, 4, 3, 2, 1
    print(t2)
    print(type(t2))

    # tupla vazia.
    t3 = tuple()
    print(t, t1, t2, t3)

    print(type(t), type(t1), type(t2), type(t3))

    # tuplas podem armazer diversos tipos:
    import os

    babel = (1, '1', [1], (1), int('1'), True, dict(), os, lambda x: print(x))

    print(babel)

if __name__ == "__main__":
    main()