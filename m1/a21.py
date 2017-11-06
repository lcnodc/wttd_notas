#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Funções
- pass: define uma function com corpo vazio.
- toda function em python retorna algo, até None
- passagem de parâmetros:
    - posicionais: a ordem importa
    - nomeados: em razão da associação explícita, a ordem não importa
    - valor default: como os atributo já é default, não é necessário informar
    - params posicionais indefinidos: atribui ao que existem e a *args o resto
    - params nomeados indeterminados: atrubuir tudo o que pode e o restante
        fica em um dict.
    - keyword only args: obrigatoriamente ter que passar args nomeados

"""


def main():
    """Definição de uma função e nomeação como main.
    Após isso, desenvolvo o corpo da função.
    """
    return 42


def foo():
    """Definição de função com corpo vazio.
    """
    pass


def positional_params(a , b , c):
    """A ordem importa.
    """
    return a , b , c


def named_params(a , c , b):
    """A ordem não importa
    """
    return a , b , c


def default_value(a , b , c=3):
    """
    """
    return a , b , c


# O args sempre uma tupla agrupa os argumentos posicionais que não têm
# correspondentes na assinatura da função
def positional_params_variable(a , b , c=3 , *args):
    """ O args é uma tupla que comporta os positional args que não têm
        correspondente na função.
    """
    return a , b , c , args


def positional_named_params_variable(a , b , c=12 , **kwargs):
    """Suporta uma quantidade indeterminada de named params.
    Tudo que não se encaixa na lista de parâmetro fica como dict.
    """
    return a , b , c , kwargs


def arg_kwargs_mix(*args , **kwargs):
    """Positional args variable e keyword args variable.
    """
    return args , kwargs


def keyword_only_args(*args , z=42 , **kwargs):
    """É um argumento que obrigatóriamente tenho que passar nomeado.
    """
    return args , z , kwargs


def sum(a , b):
    return a + b


def sub(a , b):
    return a - b


def calc(f , a , b):
    """Funções em python também são variáveis e assim podem ser passadas
    para outras funções.
    """
    return f ( a , b )


if __name__ == "__main__":
    main ( )

    # Quando não definimos o retorno a função retornará None.
    print ( foo ( ) )

    print ( positional_params ( 1 , 2 , 3 ) )

    print ( named_params ( a=1 , b=2 , c=3 ) )

    # Utilizando default value com named params.
    print ( default_value ( b=1 , a=2 ) )
    print ( default_value ( 1 , 2 ) )

    print ( positional_params_variable ( 1 , 2 , 4 , 5 , 6 , 7 , 8 ) )

    print ( positional_named_params_variable ( 1 , 2 , c=12 , d=10 , e=11 , f=12 ) )

    print ( arg_kwargs_mix ( 'a' , 'b' , a=1 , b=2 , c=3 , d=4 , e=5 ) )

    """Nesse caso se o usuário quiser passar algum parâmetro, deverá ser
        nomeado
    """
    print ( keyword_only_args ( 1 , 2 , 3 , a=33 , x=4 , y=5 , z=6 ) )

    # Outra forma de utilizar arg e kwargs mix
    t = 'a' , 'b' , 'c'
    d = dict ( z=1 , y=10 )

    # Unpacking da tupla e do dict
    print ( arg_kwargs_mix ( *t , **d ) )
    print ( arg_kwargs_mix (t, d) ) # nesse caso o dict ficará vazio.

    # tudo que for passado como nomeado será convertido para dict e depois
    # para kwargs.
    print(arg_kwargs_mix(2, 3, 4, l=1, k=2, m=3))

    print ( calc ( sum , 2 , 2 ) )
    print ( calc ( sub , 2 , 2 ) )

    import dis

    dis.dis(keyword_only_args)

    # funções podem também ser passadas como parâmetro, pois tbm são objetos.

    myfunction = lambda x, y: x + y

    def somar(func, a, b):
        print(func(a, b))


    somar(myfunction, 2, 3)