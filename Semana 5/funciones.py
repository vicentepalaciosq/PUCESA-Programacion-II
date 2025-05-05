from libro import Libro

libros=[]
isbns=[]
fechas=[]
nombres=[]

def registrar_libro():
    isbn=int(input('Ingrese el ISBN del libro: '))
    if isbn in isbns:
        print('Libro ya registrado')
    else:
        isbns.append(isbn)
        titulo=input('Ingrese el titulo del libro: ')
        autor=(input('Ingrese el autor del libro: '))
        genero=input('Ingrese el genero del libro: ')
        print('Libro registrado')
    libro=Libro(isbn, titulo, autor, genero)
    libros.append(libro)

def buscar_libro(isbn):
    for libro in libros:
        if libro.isbn == isbn:
            return libro
    return None




def registrar_prestamo():
    isbn=int(input('Ingrese el ISBN del libro: '))
    if isbn in isbns:
        nombre=input('Ingrese su nombre: ')
        nombres.append(nombre)
        fecha=input('Ingrese la fecha de retorno del libro: ')
        fechas.append(fecha)
        print('Prestamo completado')
    else:
        print('Libro no encontrado')    






def mostrar_datos():
    isbn = int(input('Ingrese el ISBN del libro: '))
    libro = buscar_libro(isbn)
    if libro:
        libro.mostrar_datos()
    else:
        print('Libro no encontrado')


def mostrar_todoslibros():
    if not isbns:
        print('No hay libros registrados')
    else: 
        for libro in libros:
            libro.mostrar_datos()

