#!/usr/bin/env python
#-*- coding: utf-8 -*-


"""
Notas do módulo 1

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
- A07                                                                        -
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Executando códigos python

$ python -c 'print(40 + 2)'

$ echo 'print(40 + 2)' | python -

$ python meuprograma.py

$ python -i meuprograma.py

# Executando o ipython

$ pip install ipython[notebook]

$ ipython

$ ipython[notebook]


-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
- A08                                                                        -
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Python em uma página

Entry point: ponto de entrada
Onde tudo começa no python, que no caso do python é o MÓDULO.
Namespace == Escopo, ambiente local de trabalho.

E quando o módulo não existe, o python cria um módulo temporário
para ser utilizado pelo interpretador. Simples assim.

Assim, tudo que for declarado dentro de um módulo, fora de uma
function, será variável global, até functions.

"""

# Importação de biblioteca os
# Biblioteca que já vem por padrão com python
# somente não é carregada.
import os


# Função principal
# Somente como referência.
# Variável global
def main():
    # Imprimindo uma string.
    print('Hello world!')
    #
    print("This Alice's greeting.")
    print('This is Bob\'s greeting.')

    foo(5, 10)

    print('=' * 10)
    # Var local
    text = 'The current working directory is '
    print(text  + os.getcwd())

    # var local
    foods = ['apples', 'oranges', 'cats']

    for food in foods:
        print('I like to eat', food)

    print('Count to ten:')
    # var local
    for i in range(1, 11):
        print(i)


# var global
def foo(a, b):
    # var local
    value = a + b

    print('%s plus %s is equal to %s' % (a, b, value))

    if value < 50:
        print('foo')
    elif (value >= 50) and \
                  ((a == 42) or (b == 24)):
        print('bar')
    else:
        print('moo')

    # Aspas triplas definem uma strig multilinha.
    '''A multi-
    line string, but can also be a
    multi-line comment.'''

    # Que tbm podem ser atribuídas a uma variável.
    ml_var = '''
    Esta é uma string multilinha
    '''
    print(ml_var)

    return value # This is a one-line comment


# __name__, var global
if __name__ == '__main__':
    main()
