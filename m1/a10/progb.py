#!/usr/bin/env python
#-*- coding: utf-8 -*-


"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
- A10                                                                        -
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
"""

# Quando esse módulo for o entry point, o nome do módulo será sempre __main__
print('Begin', __name__)

"""
Esse import também carrega e executa o módulo.
Isso acontece pq no módulo importado o código está sendo executado como
programa principal.

Quando o módulo for entry point, a execução do código é desejada.
Qdo carregado como lib, o código global do módulo não deve ser executado.
Todo o código da lib deve estar dentro de um function, caso contrário será
executado
"""
import proga


print('Define fB')

def fB():
    print('Dentro fB')
    proga.fA()
print('Chama fB')
fB()

print('End', __name__)


