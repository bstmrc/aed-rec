from registro import *
import random


def transformar_a_csv(reg):
    linea = '{},{},{}\n'.format(reg.nom, reg.gen, reg.idioma)
    return linea


def generar_csv():
    n = 100
    nom_cad = 'Macarena', 'Toxic', 'Yesterday', 'Good Vibrations', 'Respect', 'Dancing Queen', 'Bohemian Rhapsody'\
        , 'Staying Alive', 'Thriller', 'When Doves Cry', 'Like a Prayer', 'Take on me', 'With or without you', 'Wonderwall', \
              'Smells like teen spirit', 'Baby One More Time', 'Rehab', 'Rolling in the Deep', 'Poker Face', "Hips don't lie", 'Get Lucky', \
              'Shape of you'
    m = open('musica.csv', 'wt')
    for i in range(n):
        nom = random.choice(nom_cad) + str(i)
        gen = random.choice(gen_cad)
        idioma = random.choice(id_cad)
        linea = transformar_a_csv(Tema(nom, gen, idioma))
        m.write(linea)
    m.close()


def principal():
    generar_csv()


if __name__ == '__main__':
    principal()
