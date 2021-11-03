# main
import modulo as m


def main():
    opc = -1
    temas = []
    while opc != 0:
        m.print_menu()
        opc = int(input('OPCIÓN: '))
        print('--' * 40)

        if opc == 1:
            m.cargar_vector(temas, 'musica.csv')
            m.mostrar_vector(temas)

            pass

        else:
            if len(temas) == 0:
                print('ERROR: ')

            elif opc == 3:
                mat = m.generar_matriz(temas)
                m.mostrar_matriz(mat)

            elif opc == 6:
                idioma_req = int(input('Ingrese idioma que desea filtrar: '))
                m.gen_binario(idioma_req, temas)

            elif opc == 7:
                idioma_req = int(input('Ingrese idioma: '))
                m.leer_binario(idioma_req)


if __name__ == '__main__':
    main()
