from database import conectar
class AlunoDAO:

    def cadastrar(self, aluno):

        conexao = conectar()
        cursor = conexao.cursor(buffered=True)

        sql_verificar = """
        SELECT matricula FROM alunos
        WHERE matricula = %s
        """
        cursor.execute(sql_verificar, (aluno.get_matricula(),))
        existe = cursor.fetchone()

        if existe:
            cursor.close()
            conexao.close()
            return False

        sql = """
        INSERT INTO alunos (nome, curso, matricula)
        VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (aluno.get_nome(), aluno.get_curso(), aluno.get_matricula()))
        conexao.commit()

        cursor.close()
        conexao.close()
        return True
