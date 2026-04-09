import csv
from entities import Libro, Usuario

class RegistroPrestamo:
    def __init__(self, id_usuario, isbn, fecha):
        self.id_usuario = id_usuario
        self.isbn = isbn
        self.fecha = fecha
        self.activo = True

    def finalizar_registro(self): #Mark the loan as returned
        self.activo = False

    def es_de_usuario(self, id_usuario): #Check if the record belongs to a specific user
        return self.id_usuario == id_usuario

    def obtener_detalle(self): #Format the record for printing.
        estado = "ACTIVO" if self.activo else "DEVUELTO"
        return f"Usuario: {self.id_usuario} | Libro: {self.isbn} | Fecha: {self.fecha} | [{estado}]"

    def serializar(self): #Convert the object into a list for the CSV.
        return [self.id_usuario, self.isbn, self.fecha, self.activo]


class SistemaBiblioteca:
    def __init__(self, archivo_datos):
        self.archivo_datos = archivo_datos
        self.libros = []
        self.registros = []

    def registrar_libro(self, libro_obj): #Add a book to the system
        self.libros.append(libro_obj)

    def buscar_libro(self, isbn): #Will search for a book by ISBN
        for l in self.libros:
            if l.coincide_isbn(isbn):
                return l
        return None

    def procesar_prestamo(self, usuario, isbn, fecha): #The process for creating a loan/borrow and saving it in the history of the user 
        libro = self.buscar_libro(isbn)
        if libro and libro.verificar_disponibilidad():
            libro.cambiar_estado(True)
            usuario.vincular_libro(isbn)
            nuevo_registro = RegistroPrestamo(usuario.id_usuario, isbn, fecha)
            self.registros.append(nuevo_registro)
            return True
        return False

    def guardar_en_archivo(self): #Saves the loan/borrowing history to a file in the user´s profile 
        try:
            with open(self.archivo_datos, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["UsuarioID", "ISBN", "Fecha", "Activo"])
                for reg in self.registros:
                    writer.writerow(reg.serializar())
            print(f"Historial actualizado en {self.archivo_datos}")
        except IOError as e:
            print(f"Error crítico al guardar datos: {e}")