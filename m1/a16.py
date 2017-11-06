#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    """ Dicionários em python são hashmaps, armazenam pares de chaves e valores
    - Declaração através de chaves {}
    - Não mantém ordem de declaração, pois seus valores são computados com hash
    - Acesso parecido com listas, sendo acessados também pelas chaves
    - Métodos: get, keysm values, item (retornam dictionary_view), del, pop
    - Dict_views são dinâmicos, qualquer alteração no dict reflete neles
    - As chaves serão sempre objetos imutáveis
    - Outra forma de criar dict é passando uma tupla de tuplas para dict
    - Praticando ...
    """

    # Declarando...
    d = {'nome': 'luciano' , 'cidade': 'são paulo' , 'estado': 'sp' , }
    print ( d )

    # Acessando uma chave
    # Dicts não possuem um ordem,
    # Se quiser ordenã-los, terá que convertê-los em listas.
    print ( d['nome'] )
    print ( d.get ( 'estado' ) )

    # Alterando um valor
    d['cidade'] = 'Campinas'
    print ( d )

    # Acessando somente as chaves
    print ( d.keys ( ) )

    # Acessando somente os valores
    print ( d.values ( ) )

    # Contando o nro. de elementos
    print ( len ( d ) )

    # Verificando o dinamismo dos dict views
    k = d.keys ( );
    v = d.values ( );
    i = d.items ( )
    print ( k , v , i )

    d['pais'] = 'brasil'
    print ( d )
    print ( k , v , i )

    # Deletando um par
    del d['pais']
    print ( d )

    # O indice será sempre imutável
    # d[10] = 'dez' não permitido

    # Criando um dict a partir de uma tupla de tuplas.
    tdt = (('a' , 1) , ('b' , 2) , ('c' , 3) ,)
    dt = dict ( tdt )
    print ( dt )

    # Criando dicts com parâmetros nomeados
    name_dict = dict ( fabricante='volkswagen' , marca='gol' , cor='chumbo' )
    print ( name_dict )


if __name__ == "__main__":
    main ( )