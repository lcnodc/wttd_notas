#!/usr/bin/env pythonhttp.server
#-*- coding: utf-8 -*-

"""Repetições em python
- while, não se preocupa com o loop, em qual loop ele está.
- se a necessidade é contar, a melhor opção será sempre while.
- o range auxilia na criação de lista, criando a lista em real time,
economizando memória.
- enumerate auxilia em for's informando o indice o item atual
- quando usado, ele retorna um iterator e todo iterador tem uma função
dunder chamada __next__, que retorna o próximo item do iterator.
- esse retorno acontece até o momento de uma exceção do tipo StopIteration
- vale lembrar que o for, trata essa exceção
- continue e break são palavras chave que podem ser usadas junto com o for
para controlar como o for funciona
- Praticando...
"""


def main():

    # Imprimindo caracteres com while
    palavra = 'python'
    i = 0

    print(palavra, len(palavra))

    # Utilizando while, precisamos nos preocupar com o controle do loop
    while i < 6:
        print(palavra[i])
        i += 1

    # Utilizando while, agora com a função len
    i = 0
    while i < len(palavra):
        print(palavra[i])
        i += 1

    # Utilizando o for...
    for i in range(len(palavra)):
        print(palavra[i])

    # range retorna um intervalo
    r = range(10)
    print(r[2])
    print(list(r))

    # Utilização
    # range(intervalo_fechado:intervalo_aberto:passo)
    r_1k = range(0,1001,100)

    for i in r_1k:
        print(i, )

    # Mas como strings também são iteráveis...
    for c in palavra:
        print(c)

    # E caso queira o indice do str atual.
    for i, c in enumerate(palavra):
        print(i,c)

    # Caso precise controlar o loop, mesmo utilizando o for, use continue ou
    # break
    for i, c in enumerate(palavra):
        if c == 't':
            # Continua o loop pulando a execução atual
            continue
        print(i,c)

    for i, c in enumerate(palavra):
        if c == 't':
            # Interrompe o loop todo
            break
        print(i,c)

    l = [1, 2, 3]

    # Basicamente é isso que o for faz.
    # Cria uma variável para iterar
    i = 0

    # Controla a exceção do loop
    try:
        while True:
            print(l[i])
            i += 1
    except IndexError:
        pass

if __name__ == "__main__":
    main()