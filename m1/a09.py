#!/usr/bin/env python
#-*- coding: utf-8 -*-


"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
- A09                                                                        -
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Em python módulos são objetos, assim quando importando, é possível acessar
seus métodos através do operador ponto (.)

Métodos nomeados com o padrão:
    - duplo underscore | nome do método | duplo underscore

são chamados de dunders métodos, ou dundernames. Esses métodos são definidos
assim para indiciar ao programador que eles não devem ser acessados
diretamente, pois fazem parte da api interna.

O import realiza uma procura pelo módulo no diretório atual e caso não
encontrar, o python procura em diretórios padrão de sua api.

Vamos a um exemplo:

"""

from mypackage.myfunctions import hello
from math import pi

# Dessa forma, estamos importando somente a function hello do pacote mymodule

hello('Luciano')
print(pi)


"""
Em nenhuma das linhas acima foi indicado para o python, quais módulos fazem 
parte da api padrão e quais não fazem.

Mas, como o python procura sempre no diretório atual e depois em sua lib 
padrão, se os módulos existirem em algum lugar, ele sempre encontra.   

Tudo encontrado, o python carrega para o runtime e cria uma variável no 
namespace atual, referenciando o objeto lá carregado.

Veja que no runtime, o python sempre irá carregar o módulo, porém, no namespace
a decisão é sempre do programador o que carregar.
"""
