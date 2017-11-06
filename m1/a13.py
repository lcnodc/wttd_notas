#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    """Todo comando composto, entende que na próxima linha será
    iniciado um novo bloco.
    Esse novo bloco será definido por um conjunto de espaços.
    E recomenda-se espaços, pois o tab pode variar de tamanho, assim
    devemos sempre utilizar espaços.
    O pass, declarado abaixo, força a declaração de um bloco vazio.
    Na verdade, como python entende a hierarquia somente através da identação,
    quando não temos código, não temos hierarquia, assim, para fazer um bloco
    vazio, precisamos declarar a palavra pass
    """
    pass


# Linhas em branco serão ignoradas.
def foo():
    """Outro recurso utilizado é quebrar a linha do código quando ela
    excede o tamanho recomendado, 80 caracteres.
    Neste caso podemos utilizar a barra invertida (\) para quebrar a linha
    e continuar logo abaixo.
    Outra forma de fazer isso é envolver a expressão dentro de
    parenteses e quebrar sem utilizar a barra invertida. O python irá
    permitir sem problemas.
    """
    print ( 'esta é uma linha muito ' \
            'grande' )

    return ('estou' , 'aprendendo' , 'python' , 'com' , 'o' , 'welcome' ,
            'to' , 'the' , 'django.')


if __name__ == "__main__":
    main ( )
    print ( ' '.join ( foo ( ) ).capitalize ( ) )
