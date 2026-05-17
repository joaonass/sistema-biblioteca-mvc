class Emprestimo:

    def __init__(self, id_emprestimo, matricula, id_livro, data_emprestimo, data_prevista):
        self.__id_emprestimo = id_emprestimo
        self.__matricula = matricula
        self.__id_livro = id_livro
        self.__data_emprestimo = data_emprestimo
        self.__data_prevista = data_prevista

    def get_id_emprestimo(self):
        return self.__id_emprestimo

    def get_matricula(self):
        return self.__matricula

    def get_id_livro(self):
        return self.__id_livro

    def get_data_emprestimo(self):
        return self.__data_emprestimo

    def get_data_prevista(self):
        return self.__data_prevista
