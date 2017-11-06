#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
- 'in' verifica se um item está dentro de uma lista/sequence
- if, elif e else são condições utilizadas
- Qualquer resultado vazio é considerado falso
- and: o operador logico precisa que dois elementos sejam avaliados, assim o
    segundo elemento será sempre retornado. Qdo o primeiro elemento é false
    ele nem avalia o segundo elemento
- or: o mesmo acontece quando o primeiro elemento for true.
-

"""

def main():

    # Condicionais
    palavra = 'aprendendo python'

    for c in palavra:
        if c in 'eiou':
            print(c.upper(), end=' ')
        elif c in 'a':
            print(bytearray.fromhex('40').decode(), end=' ')
        elif c == 'r':
            print(bytearray.fromhex('c2ae').decode(), end=' ')
        else:
            print(c, end=' ')

    print('\n')

    # Expressões Lógicas
    print('True and True:', True and True)
    print('True and False:', True and False)
    print('True or True:', True or True)
    print('True or False:', True or False)
    print('True and []:', True and [])
    print('[] and True:', [] and True)
    print('True or ():', True or ())
    print('True or None:', True or None)
    print('[1, ] and {}:', [1, ] and {})
    print('[1, ] or {}:', [1, ] or {})


if __name__ == "__main__":
    main()
