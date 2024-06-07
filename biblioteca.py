from libro import Libro


class Biblioteca:
    def __init__(self, nombre: str, direccion: str):
        self.nombre = nombre
        self.direccion = direccion
        self.libros = []

    def agregar_libro(self, libro: Libro):
        self.libros.append(libro)
        print(f"\nEl libro {libro.titulo} se ha agregado exitosamente a la biblioteca")

    def eliminar_libro(self, titulo: str):
        libro = self.buscar_libro(titulo)
        if libro:
            self.libros.remove(libro)
            print(f"\nEl libro {libro.titulo} se ha eliminado de la biblioteca")
            return

    def buscar_libro(self, titulo: str):
        titulo_minusculas = titulo.lower().replace(" ", "")
        for libro in self.libros:
            if libro.titulo.lower().replace(" ", "") == titulo_minusculas:
                print(f"\nSe encontró el libro {libro.titulo}")
                return libro
        print(f"\nEl libro {titulo} no ha sido encontrado")
        return None

    def prestar_libro(self, titulo: str):
        libro = self.buscar_libro(titulo)
        if libro:
            if libro.disponible:
                libro.disponible = False
                print(f"\nEl libro {libro.titulo} ha sido prestado")
            else:
                print(f"El libro {libro.titulo} no esta disponible para su préstamo")

    def devolver_libro(self, titulo: str):
        libro = self.buscar_libro(titulo)
        if libro.disponible:
            print(f"\nError: El libro {libro.titulo} ya estaba disponible")
        else:
            print(f"\nEl libro {libro.titulo} ha sido devuelto")

    def mostrar_libros(self):
        if not self.libros:
            print("\nAun no hay libros en la biblioteca")
        else:
            print("\nContamos con los siguientes libros:\n")
            for libro in self.libros:
                print(libro)
                print("\n")
