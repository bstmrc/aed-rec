# modulo

from Registro import *
import pickle
import os.path


def print_menu():
    """Printea el menú principal"""
    menu = ('--' * 40) + '\n\t\t\t\t\t\t\t\tMENÚ DE OPCIONES\n' + ('--' * 40) + '\n1. \n2. \n' \
           + '3. \n4. \n5. \n' \
           + '6. Generar binario por idioma\n7. Leer binario\n0. SALIR\n' + ('--' * 40)

    print(menu)


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


def gen_fd(i):
    fd = 'MusicaIdioma' + str(i) + '.dat'
    return fd 


def gen_binario(i, vec):
    fd = gen_fd(i)
    
    m = open(fd, 'wb')

    for item in vec:
        if item.idioma == i:
            pickle.dump(item, m)

    m.close()


def leer_binario(i):
    fd = gen_fd(i)
    tam = os.path.getsize(fd)

    m = open(fd, 'rb')

    while m.tell() < tam:
        item = pickle.load(m)
        print(item)

    m.close()


def generar_matriz(v):
    mat = [[0] * 5 for i in range(6)]
    for i in range(len(v)):
        f = v[i].gen
        c = v[i].idioma
        mat[f][c] += 1
    return mat


def mostrar_matriz(mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            if mat[f][c] != 0:
                write(f, c, mat)


def write(f, c, mat):
    s = '|Genero:{:<15} |Idioma: {:<15} |Canridad de temas: {:>3}'
    s = s.format(gen_cad[f], id_cad[c], mat[f][c])
    print(s)


def principal():
    v = []
    print('prueba')
    cargar_vector(v, 'musica.csv')
    mostrar_vector(v)
    i = int(input('Idioma: '))
    gen_binario(i, v)
    leer_binario(i)


if __name__ == '__main__':
    principal()
