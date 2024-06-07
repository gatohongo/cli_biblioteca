class Libro:
    def __init__(self, titulo: str, autor: str, anio_publicacion: int, disponible: bool):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.disponible = disponible

    def __str__(self) -> str:
        return (f"Titulo: {self.titulo} \nAutor: {self.autor} \n"
                f"Año de publicación: {self.anio_publicacion} \nDisponible: {self.disponible}")
