# modulo

from Registro import *
import pickle
import os.path


































































def gen_binario(i, vec):

    fd = 'MusicaIdioma' + str(i) + '.dat'
    
    m = open(fd, 'wb')

    for item in vec:
        if item.idioma == i:
            pickle.dump(i, m)
            pickle.dump('\n', m)

    m.close()


