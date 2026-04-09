import csv
from entities import Libro, Usuario

class RegistroPrestamo:
    def __init__(self, id_usuario, isbn, fecha):
        self.id_usuario = id_usuario
        self.isbn = isbn
        self.fecha = fecha
        self.activo = True

    def finalizar_registro(self):
        #"""Marca el préstamo como devuelto."""
        self.activo = False

    def es_de_usuario(self, id_usuario):
        #"""Comprueba si el registro pertenece a un usuario específico."""
        return self.id_usuario == id_usuario

    def obtener_detalle(self):
        #"""Formatea el registro para impresión."""
        estado = "ACTIVO" if self.activo else "DEVUELTO"
        return f"Usuario: {self.id_usuario} | Libro: {self.isbn} | Fecha: {self.fecha} | [{estado}]"

    def serializar(self):
        #"""Convierte el objeto en una lista para el CSV."""
        return [self.id_usuario, self.isbn, self.fecha, self.activo]


class SistemaBiblioteca:
    def __init__(self, archivo_datos):
        self.archivo_datos = archivo_datos
        self.libros = []
        self.registros = []

    def registrar_libro(self, libro_obj):
        #"""Añade un libro a la colección."""
        self.libros.append(libro_obj)

    def buscar_libro(self, isbn):
        #"""Busca un libro por ISBN usando estructuras de control."""
        for l in self.libros:
            if l.coincide_isbn(isbn):
                return l
        return None

    def procesar_prestamo(self, usuario, isbn, fecha):
        #"""Lógica para generar un préstamo y guardarlo en el historial."""
        libro = self.buscar_libro(isbn)
        if libro and libro.verificar_disponibilidad():
            libro.cambiar_estado(True)
            usuario.vincular_libro(isbn)
            nuevo_registro = RegistroPrestamo(usuario.id_usuario, isbn, fecha)
            self.registros.append(nuevo_registro)
            return True
        return False

    def guardar_en_archivo(self):
        #"""Guarda el historial de préstamos en un archivo (Data Handling)."""
        try:
            with open(self.archivo_datos, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["UsuarioID", "ISBN", "Fecha", "Activo"])
                for reg in self.registros:
                    writer.writerow(reg.serializar())
            print(f"Historial actualizado en {self.archivo_datos}")
        except IOError as e:
            # Requisito 5: Manejo de excepciones
            print(f"Error crítico al guardar datos: {e}")