#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""Example de módulo em python

Este exemplo define um módulo com uma função que pode ser importada em um
programa python.

"""
def hello(msg):
    '''Função hello
    :param msg: Uma string representando o nome de algo ou algupém.
    :return: Uma string representando uma saudação a algo ou alguém.
    '''
    print('Hello {}'.format(msg))
