from entities import Libro, Usuario
from manager import SistemaBiblioteca

def iniciar(): #System´s activation 
    sistema = SistemaBiblioteca("historial_prestamos.csv")

    # Creation of books, writer´s name, isbn and users name and number of client 
    libro1 = Libro("123-1", "Cien años de soledad", "G. García Márquez")
    libro2 = Libro("124-2", "Don Quijote", "Miguel de Cervantes")
    user1 = Usuario("Numero de cliente 1", "Carlos Pérez")

    sistema.registrar_libro(libro1)
    sistema.registrar_libro(libro2)

    # Book´s borrowing process 
    print("--- Gestión de Préstamos ---")
    if sistema.procesar_prestamo(user1, "123-1", "09/04/2026"):
        print(f"Préstamo exitoso para: {user1.nombre}")
    else:
        print("El libro no está disponible.")

    #  Shows if the book isn´t available 
    print("\nEstado de los libros:")
    for lib in sistema.libros:
        print(lib.obtener_info())

    print("\nResumen del Usuario:")
    print(user1.resumen_usuario())

    # Record Keeping
    print("\nSincronizando con base de datos...")
    sistema.guardar_en_archivo()

if __name__ == "__main__":
    iniciar()