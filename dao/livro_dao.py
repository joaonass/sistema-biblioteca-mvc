from database import conectar

class LivroDAO:

    def cadastrar(self, livro):

        conexao = conectar()
        cursor = conexao.cursor(buffered=True)

        try:
            sql_verificar = """
            SELECT id_livro FROM livros
            WHERE id_livro = %s
            """
            cursor.execute(sql_verificar, (livro.get_id_livro(),))
            existe = cursor.fetchone()

            if existe:
                return False

            sql = """
            INSERT INTO livros (id_livro, titulo, autor, quantidade)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (
                livro.get_id_livro(),
                livro.get_titulo(),
                livro.get_autor(),
                livro.get_quantidade()
            ))

            conexao.commit()
            return True

        finally:
            cursor.close()
            conexao.close()

    def atualizar_quantidade(self, id_livro, valor):

        conexao = conectar()
        cursor = conexao.cursor(buffered=True)

        try:
            sql = """
            UPDATE livros
            SET quantidade = quantidade + %s
            WHERE id_livro = %s
            """
            cursor.execute(sql, (valor, id_livro))
            conexao.commit()

        finally:
            cursor.close()
            conexao.close()
