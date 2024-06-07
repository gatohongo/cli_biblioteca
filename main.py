from time import sleep
from biblioteca import Biblioteca
from libro import Libro


def main():
    # Se crea el objeto de la clase Biblioteca
    biblioteca = Biblioteca("Biblioteca Pública Virgilio Barco", "Carrera 60 #57-60")

    ejecutando = True
    while ejecutando:
        try:
            print("\nBienvenido a nuestro servicio de biblioteca. ¿Qué desea realizar?")
            print("1. Agregar un libro")
            print("2. Eliminar un libro")
            print("3. Buscar un libro")
            print("4. Prestar un libro")
            print("5. Devolver un libro")
            print("6. Mostrar los libros")
            print("7. Salir\n")
            opcion = int(input("Digite el numero de la opcion que desea realizar: "))

            match opcion:
                case 1:
                    titulo = input("Ingrese el titulo del libro: ")
                    autor = input("Ingrese el autor del libro: ")
                    anio_publicacion = int(input("Ingrese la fecha de publicacion del libro: "))
                    libro = Libro(titulo, autor, anio_publicacion, True)
                    biblioteca.agregar_libro(libro)
                    sleep(1)

                case 2:
                    titulo = input("Ingrese el titulo del libro: ")
                    biblioteca.eliminar_libro(titulo)
                    sleep(1)

                case 3:
                    titulo = input("Ingrese el titulo del libro: ")
                    biblioteca.buscar_libro(titulo)
                    sleep(1)

                case 4:
                    titulo = input("Ingrese el titulo del libro: ")
                    biblioteca.prestar_libro(titulo)
                    sleep(1)

                case 5:
                    titulo = input("Ingrese el titulo del libro: ")
                    biblioteca.devolver_libro(titulo)
                    sleep(1)

                case 6:
                    biblioteca.mostrar_libros()
                    sleep(1)

                case 7:
                    print("\nSaliendo de la aplicacion...")
                    ejecutando = False

        except ValueError:
            print("Error en la digitación, vuelva a intentarlo")
            sleep(1)


if __name__ == "__main__":
    main()
