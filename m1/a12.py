#!/usr/bin/env python
#-*- coding: utf-8 -*-

def main():

    # String são objetos, mas também são sequências.
    # Assim, elas podem ser tratadas de tal forma, sendo acessadas como array.
    # Primeiro caracter é o indice 0 e o último -1.
    # Podemos também fatiar essas string com a notação :
    # Outra característica é que a string já sabe seu próprio tamanho.
    # Assim, quando precisamos deve valor, podemos omití-lo.
    # Outra caracteristica no python, é que existem diversas sintaxes que são
    # atalhos para as funções que realmente existem em um nível mais baixo.
    # Um exemplo é o acesso a indices com colchetes que é traduzido na função
    # __getitem__.
    # Outro exemplo, é o fatiamento que pode ser realizado utilizando a notação
    # :. É claro que isso é somente um açúcar sintático para o __getitem__
    # recebendo como parâmetro um objeto slice, que retorna uma 'fatia' da str.
    message = "estou aprendendo python"

    # Consultando o tamanho da str.
    print(len(message))

    # Acessando um item da str/sequence
    print(message[2])

    # Acessando o último elemento
    print(message[-1])

    # Fatiando a sequence
    print(message[:2])
    print(message[1:2])

    # O terceiro elemento representa o passo.
    # str[start:stop:step]
    print(message[1:-1:2])

    # Como vimos, os colchetes são atalhos para métodos internos, aqueles com
    # dunders names, que nunca devem ser acessados diretamente.


if __name__ == "__main__":
    main()