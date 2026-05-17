from model.aluno import Aluno
from dao.aluno_dao import AlunoDAO

class AlunoController:

    def __init__(self):
        self.dao = AlunoDAO()

    def cadastrar(self, nome, curso, matricula):

        if nome == "" or curso == "" or matricula == "":
            return "CAMPOS"

        aluno = Aluno(nome, curso, matricula)

        if self.dao.cadastrar(aluno):
            return "OK"
        return "EXISTE"
