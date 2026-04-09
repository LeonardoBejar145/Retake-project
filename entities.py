class Libro:
    def __init__(self, isbn, titulo, autor):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.esta_prestado = False

    def cambiar_estado(self, prestado: bool):
        #"""Actualiza la disponibilidad del libro."""
        self.esta_prestado = prestado

    def obtener_info(self):
        #"""Retorna una cadena con los datos del libro."""
        estado = "Prestado" if self.esta_prestado else "Disponible"
        return f"[{self.isbn}] {self.titulo} - {self.autor} ({estado})"

    def verificar_disponibilidad(self):
        #"""Indica si el libro se puede prestar."""
        return not self.esta_prestado

    def coincide_isbn(self, isbn_buscado):
        #"""Valida si el ISBN coincide para búsquedas."""
        return self.isbn == isbn_buscado


class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.libros_activos = []

    def vincular_libro(self, isbn):
        #"""Agrega un ISBN a la lista del usuario."""
        self.libros_activos.append(isbn)

    def desvincular_libro(self, isbn):
        #"""Quita un ISBN de la lista del usuario."""
        if isbn in self.libros_activos:
            self.libros_activos.remove(isbn)
            return True
        return False

    def tiene_libros(self):
        #"""Verifica si el usuario tiene préstamos pendientes."""
        return len(self.libros_activos) > 0

    def resumen_usuario(self):
        #"""Retorna el perfil del usuario."""
        return f"ID: {self.id_usuario} | Nombre: {self.nombre} | Libros: {len(self.libros_activos)}"