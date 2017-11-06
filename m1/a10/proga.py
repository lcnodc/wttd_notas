#!/usr/bin/env python
#-*- coding: utf-8 -*-


"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
- A10                                                                        -
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
"""

# Início do código global
print('Begin', __name__)

print('Define fA')
# Fim do código global
def fA():
    print('Dentro fA')


# O if define se o módulo atual é o entry point. Caso negativo, o código global
# não será executado.
if __name__ == '__main__':
    print('Chama fA')
    fA()

print('End', __name__)
