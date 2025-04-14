class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio=anio
    def datos(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Año: {self.anio}"

libro1=Libro('Cuamanda','Juan Leon Mera', '1879')
libro2=Libro('El principito','Antoine de Saint-Exupéry', '1943' )

print(libro1.datos())
print(libro2.datos())