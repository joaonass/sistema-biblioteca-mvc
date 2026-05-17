class Livro:

    def __init__(self, id_livro, titulo, autor, quantidade):
        self.__id_livro = id_livro
        self.__titulo = titulo
        self.__autor = autor
        self.__quantidade = quantidade

    def get_id_livro(self):
        return self.__id_livro

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_quantidade(self):
        return self.__quantidade
