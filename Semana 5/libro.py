

class Libro:
    def __init__(self, titulo, autor, isbn, genero):
        self.titulo= titulo
        self.autor=autor
        self.isbn=isbn
        self.genero=genero
        self.prestamos=[]
        self.fechas=[]
        self.nombres=[]
        

    def agregar_prestamo(self, titulo, isbn, prestamos):
        prestamoss = {
            "titulo": titulo,
            "isbn": isbn,
            "prestamos": prestamos
        }
        self.prestamos.append(prestamoss)



    def mostrar_datos(self):
        print('Titulo del libro: ', self.titulo)
        print('Autor: ', self.autor)
        print('Genero: ', self.genero)
