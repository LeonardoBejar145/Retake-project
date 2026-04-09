class Libro:
    def __init__(self, isbn, titulo, autor):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.esta_prestado = False

    def cambiar_estado(self, prestado: bool): #Is going to uppdate the availability of the book 
        self.esta_prestado = prestado

    def obtener_info(self): #Returns a string containing the book's data in case is or is not available
        estado = "Prestado" if self.esta_prestado else "Disponible"
        return f"[{self.isbn}] {self.titulo} - {self.autor} ({estado})"

    def verificar_disponibilidad(self): # Indicates if the book is available 
        return not self.esta_prestado

    def coincide_isbn(self, isbn_buscado): #Validate if the ISBN matches for searches
        return self.isbn == isbn_buscado


class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.libros_activos = []

    def vincular_libro(self, isbn): #Adds an ISBN to the user's list in case he wants to take the book 
        self.libros_activos.append(isbn)

    def desvincular_libro(self, isbn): #Remove an ISBN from the user's list in case he give it back
        if isbn in self.libros_activos:
            self.libros_activos.remove(isbn)
            return True
        return False

    def tiene_libros(self): #Check if the user has any other book in use 
        return len(self.libros_activos) > 0

    def resumen_usuario(self): #Shows the user's profile
        return f"ID: {self.id_usuario} | Nombre: {self.nombre} | Libros: {len(self.libros_activos)}"