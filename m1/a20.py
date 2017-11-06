#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""Atribuições
- é possível atribuir uma sequence a diversas variáveis, desde que com tamanho
    compatíveis
- caso queira atribuir itens dispares a uma certa qtde de variáveis, usamos o _
- *_ ou *wherever, define ao python que irá receber tudo menos o já atribuído

"""

def main():

    # Temos uma tupla e temos que atribuir um item a cada var.
    tupla = 'linux', 'python', 'sublime', 'django'

    # Forma 1
    sistema, linguagem, editor, framework = tupla[0], tupla[1], tupla[2], \
        tupla[3]
    print(sistema, linguagem, editor, framework)

    # Forma 2
    sistema, linguagem, editor, framework = tupla
    print(sistema, linguagem, editor, framework)

    # Forma 3: Nesse exemplo a qtde. de vars será menor.
    sistema, linguagem = tupla[0:2]
    print(sistema, linguagem)

    # Forma 4: Nesse exemplo a ordem não é sequêncial.
    sistema, _, editor, _ = tupla
    print(sistema, editor)

    # Forma 5: Nesse exemplo a ordem é sequêncial, mas não somente os últimos.
    # e isso vale para os primeiros itens também.
    *_,  editor, framework = tupla
    print(editor, framework)

    # Agora vamos utilizar o for para percorrer uma tupla mais complexa.
    table = (('linux', 'python', 'sublime', 'django'),
             ('windows', 'c#', 'visual studio', '.net'))

    # Forma 1: unpacking por tupla
    for line in table:
        print(line)

    # Forma 2: unpacking individual
    for sistema, linguagem, editor, framework in table:
        print(sistema, linguagem, editor, framework)

    # Forma 3: tudo já visto, serve para o for tbm.
    # O restante dos itens da tupla são atribuidos ao underscore
    for sistema, *_ in table:
        print(sistema)


if __name__ == "__main__":
    main()
