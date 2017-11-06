#!/usr/bin/env python
#-*- coding: utf-8 -*-


def main():
    """Em python a tipagem é dinâmica
    - O python identifica o objeto associado com letras e a partir dai
    disponibiliza os métodos
    - Tipagem forte, não converte de forma implícita
    - Com python também é possível fazer sobrecarga de operadores.
    - Assim, podemos utilizar operadores padrão para criar comportamentos
    distintos em nossas classes. Porém tudo tem um limite.
    -
    """

    # declarando uma variável
    valor = 1
    print(1)
    print(type(1))

    letras = 'abc'
    print(letras)

    # Identificando qual objeto está associado à variável letras
    print(letras.upper)

    # Tipagem forte
    # print(1 + '1') # Error
    # Sou obrigado a  definir previamente o que eu quero.
    # Aqui é criado um objeto do tipo inteiro, e não convertido.
    # Outro ponto, é a sobrecarga de operadores, pois o + concatena e soma
    # ao mesmo tempo, e seu comportamento dependerá do tipo de objeto que
    # estiver utilizando ele.
    print(1 + int('1'))
    print(str(1) + '1')

    # Isso é um açúcar sintático para ...
    print(int(1).__add__(int('1')))
    print(str(1).__add__(str(1)))

    # Isso acontece também para: % (__mod__), * (__mult__), - (__sub__), etc...


if __name__ == "__main__":
    main()