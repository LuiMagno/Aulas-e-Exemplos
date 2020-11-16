# Métodos especiais são métodos que permitem a classe ter comportamentos diferentes quando a classe for utilizado com métodos embutidos no python
class Book(object):
    def __init__(self, titulo,autor,paginas):
        print('Um livro foi criado.')
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    def __str__(self):
        return 'Titulo {a}'.format(a = self.titulo)
livro = Book('Fantasia louca', 'Lui Magno', 1000)

print(livro) #vimos aqui que graças ao str na linha 8 o método print funciona de forma diferente na classe Book

# Resumindo, nós podemos mudar o funcionamento de método embutidos do python, como print,len,del, input e por ai vai.