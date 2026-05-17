from database import conectar

class EmprestimoDAO:

    def cadastrar(self, emprestimo):

        conexao = conectar()
        cursor = conexao.cursor(buffered=True)

        sql_verificar = """
        SELECT id_emprestimo FROM emprestimos
        WHERE id_emprestimo = %s
        """
        cursor.execute(sql_verificar, (emprestimo.get_id_emprestimo(),))
        existe = cursor.fetchone()

        if existe:
            cursor.close()
            conexao.close()
            return False

        sql_verificar_livro = """
        SELECT quantidade FROM livros
        WHERE id_livro = %s
        """
        cursor.execute(sql_verificar_livro, (emprestimo.get_id_livro(),))
        livro = cursor.fetchone()

        if livro is None or livro[0] <= 0:
            cursor.close()
            conexao.close()
            return None

        sql = """
        INSERT INTO emprestimos
        (id_emprestimo, id_aluno, id_livro, data_emprestimo, data_prevista_devolucao, data_devolucao)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (
            emprestimo.get_id_emprestimo(),
            emprestimo.get_matricula(),
            emprestimo.get_id_livro(),
            emprestimo.get_data_emprestimo(),
            emprestimo.get_data_prevista(),
            None
        ))

        sql_update = """
        UPDATE livros
        SET quantidade = quantidade - 1
        WHERE id_livro = %s
        """
        cursor.execute(sql_update, (emprestimo.get_id_livro(),))

        conexao.commit()
        cursor.close()
        conexao.close()
        return True

    def devolver(self, id_emprestimo):

        conexao = conectar()
        cursor = conexao.cursor(buffered=True)

        sql_buscar = """
        SELECT id_livro, data_devolucao
        FROM emprestimos
        WHERE id_emprestimo = %s
        """
        cursor.execute(sql_buscar, (id_emprestimo,))
        resultado = cursor.fetchone()

        if resultado is None:
            cursor.close()
            conexao.close()
            return "NAO_EXISTE"

        id_livro = resultado[0]
        data_devolucao = resultado[1]

        if data_devolucao is not None:
            cursor.close()
            conexao.close()
            return "JA_DEVOLVIDO"

        sql_devolver = """
        UPDATE emprestimos
        SET data_devolucao = CURDATE()
        WHERE id_emprestimo = %s
        """
        cursor.execute(sql_devolver, (id_emprestimo,))

        sql_livro = """
        UPDATE livros
        SET quantidade = quantidade + 1
        WHERE id_livro = %s
        """
        cursor.execute(sql_livro, (id_livro,))

        conexao.commit()
        cursor.close()
        conexao.close()
        return "DEVOLVIDO"

    def consultar(self, id_emprestimo):

        conexao = conectar()
        cursor = conexao.cursor(buffered=True)

        sql = """
        SELECT 
            e.id_emprestimo,
            e.id_aluno,
            a.nome,
            e.id_livro,
            l.titulo,
            e.data_emprestimo,
            e.data_prevista_devolucao,
            e.data_devolucao
        FROM emprestimos e
        INNER JOIN alunos a ON e.id_aluno = a.matricula
        INNER JOIN livros l ON e.id_livro = l.id_livro
        WHERE e.id_emprestimo = %s
        """
        cursor.execute(sql, (id_emprestimo,))
        resultado = cursor.fetchone()

        cursor.close()
        conexao.close()
        return resultado
