from datetime import datetime
from model.emprestimo import Emprestimo
from dao.emprestimo_dao import EmprestimoDAO

class EmprestimoController:

    def __init__(self):
        self.dao = EmprestimoDAO()

    def validar_data(self, data_texto):
        try:
            return datetime.strptime(data_texto, "%Y-%m-%d").date()
        except:
            return None

    def realizar(self, id_emprestimo, matricula, id_livro, data_emprestimo, data_prevista):

        if id_emprestimo == "" or matricula == "" or id_livro == "" or data_emprestimo == "" or data_prevista == "":
            return "CAMPOS"

        data_emp = self.validar_data(data_emprestimo)
        data_prev = self.validar_data(data_prevista)

        if data_emp is None or data_prev is None:
            return "DATA"

        if data_prev < data_emp:
            return "MENOR"

        emprestimo = Emprestimo(id_emprestimo, matricula, id_livro, data_emp, data_prev)

        resultado = self.dao.cadastrar(emprestimo)

        if resultado is True:
            return "OK"
        if resultado is False:
            return "EXISTE"
        return "INDISPONIVEL"

    def devolver(self, id_emprestimo):
        if id_emprestimo == "":
            return "CAMPOS"
        return self.dao.devolver(id_emprestimo)

    def consultar(self, id_emprestimo):
        if id_emprestimo == "":
            return None
        return self.dao.consultar(id_emprestimo)
