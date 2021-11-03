# registro
gen_cad = '0-Balada', '1-Pop', '2-Rock', '3-Folclore', '4-Electrónica', '5-Otros'
id_cad = '0-Español', '1-Inglés', '2-Francés', '3-Portugués', '4-Otros'


class Tema:
    def __init__(self, nom, gen, idioma):
        self.nom = nom
        self.gen = gen
        self.idioma = idioma

    def __str__(self):
        s = '|Título:{:<30} |Género: {:<15} |Idioma: {:>3}'
        s = s.format(self.nom, gen_cad[self.gen], id_cad[self.idioma])
        return s
