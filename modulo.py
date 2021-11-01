# modulo

from Registro import *
import pickle
import os.path


def add_in_order(v, reg):
    izq, der = 0, len(v) - 1
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if reg.nom == v[c].nom:
            pos = c
            break
        if reg.nom < v[c].nom:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [reg]


def csv_a_vec(line):
    if line[-1] == '\n':
        line = line[:-1]
    campos = line.split(',')
    return Tema(campos[0], int(campos[1]), int(campos[2]))


def cargar_vector(v, fd):
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe')
    else:
        m = open(fd, 'rt')
        for line in m:
            reg = csv_a_vec(line)
            add_in_order(v, reg)
        m.close()


def mostrar_vector(v):
    for i in range(len(v)):
        print(v[i])


def gen_binario(i, vec):

    fd = 'MusicaIdioma' + str(i) + '.dat'
    
    m = open(fd, 'wb')

    for item in vec:
        if item.idioma == i:
            pickle.dump(i, m)
            pickle.dump('\n', m)

    m.close()


def principal():
    v = []
    print('prueba')
    cargar_vector(v, 'musica.csv')
    mostrar_vector(v)
    i = int(input('Idioma: '))
    gen_binario(i, v)


if __name__ == '__main__':
    principal()
