from model.livro import Livro
from dao.livro_dao import LivroDAO

class LivroController:

    def __init__(self):
        self.dao = LivroDAO()

    def cadastrar(self, id_livro, titulo, autor, quantidade):

        if id_livro == "" or titulo == "" or autor == "" or quantidade == "":
            return "CAMPOS"

        try:
            quantidade = int(quantidade)
            if quantidade < 0:
                return "NEGATIVO"
        except:
            return "NUMERO"

        livro = Livro(id_livro, titulo, autor, quantidade)

        if self.dao.cadastrar(livro):
            return "OK"
        return "EXISTE"
