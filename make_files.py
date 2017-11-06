#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Cria os arquivos das notas, referente à quantidade aulas.

'''

import sys

def main():

    hashbang_ = '#!/usr/bin/env python\n# -*- coding: utf-8 -*-'

    if len(sys.argv) != 2:
        sys.exit('usage ./make_files name_dir')

    dir_ = sys.argv[1]
    start = sys.argv[2]
    end = sys.argv[3]

    for i in range(start, end):
        with open(''.join([dir_, '/', 'a', str(i), '.py']), 'w') as file_:
            file_.write(hashbang_)


if __name__ == '__main__':
    main()