class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def mostrar(self):
        print(f"'{self.titulo}' fue escrito por {self.autor} en el año {self.año}.")


libro1=Libro('Mi pluma lo mato', 'Juan Montalvo', '1875')
libro2=Libro('Cumanda','Juan Leon Mera', '1879')

libro1.mostrar()
libro2.mostrar()