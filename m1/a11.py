#!/usr/bin/env python
#-*- coding: utf-8 -*-

def main():

    # Utilizar aspas simples ou duplas.
    print("Imprimindo uma nova string")
    print('Imprimindo uma nova string')

    # Strings em python são objetos de alto nível.
    print("Luciano".encode())

    # Podemos representar qualquer caracter utilizando string em python.
    print("こんにちは世界")

    # Existem diversas funções de manipulação de strings em python, mas
    # qualquer mudança que ocorrer na strings será gerado outro objeto
    # pois em python string são imutáveis.
    print("luciano cunha".title())

    # Um exemplo disso...
    nome = 'luciano cunha'
    print(id(nome))
    print(id(nome.title()))
    nome = 'meu nome'
    print(id(nome))

    # algumas functions de string:
    # replace, split, capitalize, title(), join, len

    # Join é forma mais correta de concatenar strings, apesar de ser possível
    # fazê-lo com o operador +.

    # outros métodos de string
    print('luciano'.replace('u', 'l'))
    print(' '.join(['luciano', 'cunha']))

    # para junções de string é sempre melhor utilizar o join
    print('\n'.join(['luciano', 'cunha']))

    # comprimento da string
    print(len('luciano'))

if __name__ == "__main__":
    main()
