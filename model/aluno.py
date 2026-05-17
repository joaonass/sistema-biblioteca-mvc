class Aluno:

    def __init__(self, nome, curso, matricula):
        self.__nome = nome
        self.__curso = curso
        self.__matricula = matricula

    def get_nome(self):
        return self.__nome

    def get_curso(self):
        return self.__curso

    def get_matricula(self):
        return self.__matricula
