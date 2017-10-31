#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
Kata: A arte marcial na programação.

Regras Estabelecidas do Fizzbuzz

1. Se posição for múltipla de 3: fizz
2. Se a posição for múltipla de 5: buzz
3. Se a posição for múltipla de 3 e 5: fizzbuzz
4. Para qualquer outra posição fale o próprio n.

Notas:

- O código deve ser feito passo a passo.
- Resolvendo um erro para somente depois passar para o próximo.
- Procure resolver específicamente o erro informado, o menor passo necessário.
- O objetivo será sempre estabilizar o código,
- Estabilizado o código e alcançado o objetivo, o próximo passo consiste em:
    - Novos testes; ou
    - Refatorar o código.
- A princípio pode parecer lento, mas a ideia é ir esculpindo o código a
    partir da demanda que o teste vai criando.
- A simplicidade é fundamental.
- Procure generalizar o código o melhor possível.
- TDD não é realizar todos os testes possíveis, mas sim, conhecer os limites do
    problema e do comportamento do código desenvolvido.

- Pontos a se atentar no código:
    - O ideal é que as funções tenham somente um ponto de saída, um return.
    - Utilize funções auxiliares.


Em funções def pode-se colocar:
    -  expressões (num % base == 0); ou
    - comandos (return)

O lambda: não suporta statements / return / if / for, somente expressões no
    corpo da função.

functools, partial: Recebe uma função e args e retorna uma nova função, que
    considera os args passados.

Quando o lambda é executado o retorno é o resultado da redução da avalição
    dessa expressão, que é o corpo da função.

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
- ASSERTIONERROR:                                                             -
=                                                                             =
- É a falha da espectativa. Ou seja, o estabelecido não está sendo atendido.  -
=                                                                             =
- QUALQUER OUTRA EXCEPTION É O CHAMADO 'ERRO':                                -
=                                                                             =
- Todo erro diferente de assertionerror é ERRO, ocasionado por alguma coisa no-
= código que quebrou.                                                         =
-                                                                             -
= Resolvê-lo será sempre mais prioritário.                                    =
-                                                                             -
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

"""

from functools import partial


multiple_of = lambda  base, num: num % base == 0
multiple_of_5 = partial(multiple_of, 5)
multiple_of_3 = partial(multiple_of, 3)


def robot(pos):
    say = str(pos)

    if multiple_of_3(pos) and multiple_of_5(pos):
        say = 'fizzbuzz'
    elif multiple_of_5(pos):
        say = 'buzz'
    elif multiple_of_3(pos):
        say  = 'fizz'

    return say


if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(12) == 'fizz'
    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'

