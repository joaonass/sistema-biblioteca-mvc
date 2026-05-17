import tkinter as tk
from tkinter import messagebox

from controller.aluno_controller import AlunoController
from controller.livro_controller import LivroController
from controller.emprestimo_controller import EmprestimoController


class TelaSistema:

    def __init__(self):

        self.aluno_controller = AlunoController()
        self.livro_controller = LivroController()
        self.emprestimo_controller = EmprestimoController()

        self.janela = tk.Tk()
        self.janela.title("Sistema Biblioteca")
        self.janela.geometry("1200x700")
        self.janela.configure(bg="#1e1e2e")
        self.janela.resizable(False, False)

        self.frame_menu = tk.Frame(self.janela, bg="#1e1e2e")
        self.frame_aluno = tk.Frame(self.janela, bg="#1e1e2e")
        self.frame_livro = tk.Frame(self.janela, bg="#1e1e2e")
        self.frame_emprestimo = tk.Frame(self.janela, bg="#1e1e2e")
        self.frame_devolucao = tk.Frame(self.janela, bg="#1e1e2e")
        self.frame_consulta = tk.Frame(self.janela, bg="#1e1e2e")

        self.criar_interface()

    def esconder_frames(self):
        self.frame_menu.pack_forget()
        self.frame_aluno.pack_forget()
        self.frame_livro.pack_forget()
        self.frame_emprestimo.pack_forget()
        self.frame_devolucao.pack_forget()
        self.frame_consulta.pack_forget()

    def mostrar_frame(self, frame):
        self.esconder_frames()
        frame.pack(fill="both", expand=True)
        frame.pack_propagate(False)

    def voltar_menu(self):
        self.mostrar_frame(self.frame_menu)

    def abrir_aluno(self):
        self.mostrar_frame(self.frame_aluno)

    def abrir_livro(self):
        self.mostrar_frame(self.frame_livro)

    def abrir_emprestimo(self):
        self.mostrar_frame(self.frame_emprestimo)

    def abrir_devolucao(self):
        self.mostrar_frame(self.frame_devolucao)

    def abrir_consulta(self):
        self.mostrar_frame(self.frame_consulta)

    def criar_botao_menu(self, texto, comando):
        return tk.Button(
            self.menu_container,
            text=texto,
            command=comando,
            font=("Arial", 16, "bold"),
            width=30,
            height=2,
            bg="#4a90e2",
            fg="white",
            activebackground="#357ABD",
            activeforeground="white",
            bd=0,
            relief="flat",
            cursor="hand2"
        )

    def salvar_aluno(self):

        nome = self.entry_nome.get()
        curso = self.entry_curso.get()
        matricula = self.entry_matricula.get()

        resultado = self.aluno_controller.cadastrar(nome, curso, matricula)

        if resultado == "CAMPOS":
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        if resultado == "EXISTE":
            messagebox.showerror("Erro", "Essa matrícula já existe!")
            return

        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")

        self.entry_nome.delete(0, tk.END)
        self.entry_curso.delete(0, tk.END)
        self.entry_matricula.delete(0, tk.END)

    def salvar_livro(self):

        id_livro = self.entry_idLivro.get()
        titulo = self.entry_nomeLivro.get()
        autor = self.entry_nomeAutor.get()
        quantidade = self.entry_quantidadeLivro.get()

        resultado = self.livro_controller.cadastrar(id_livro, titulo, autor, quantidade)

        if resultado == "CAMPOS":
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        if resultado == "NUMERO":
            messagebox.showerror("Erro", "Quantidade deve ser numérica!")
            return

        if resultado == "NEGATIVO":
            messagebox.showerror("Erro", "Quantidade não pode ser negativa!")
            return

        if resultado == "EXISTE":
            messagebox.showerror("Erro", "Esse ID de livro já existe!")
            return

        messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")

        self.entry_nomeLivro.delete(0, tk.END)
        self.entry_nomeAutor.delete(0, tk.END)
        self.entry_quantidadeLivro.delete(0, tk.END)
        self.entry_idLivro.delete(0, tk.END)

    def realizar_emprestimo(self):

        id_emprestimo = self.entry_idEmprestimo.get()
        matricula = self.entry_matriculaAluno.get()
        id_livro = self.entry_idLivroEmp.get()
        data_emprestimo = self.entry_dataEmprestimo.get()
        data_prevista = self.entry_dataPrevista.get()

        resultado = self.emprestimo_controller.realizar(
            id_emprestimo,
            matricula,
            id_livro,
            data_emprestimo,
            data_prevista
        )

        if resultado == "CAMPOS":
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        if resultado == "DATA":
            messagebox.showerror("Erro", "Formato inválido! Use AAAA-MM-DD")
            return

        if resultado == "MENOR":
            messagebox.showerror("Erro", "A data prevista não pode ser menor que a data do empréstimo!")
            return

        if resultado == "EXISTE":
            messagebox.showerror("Erro", "Esse ID de empréstimo já existe!")
            return

        if resultado == "INDISPONIVEL":
            messagebox.showerror("Erro", "Livro não encontrado ou indisponível!")
            return

        messagebox.showinfo("Sucesso", "Empréstimo realizado!")

        self.entry_idEmprestimo.delete(0, tk.END)
        self.entry_matriculaAluno.delete(0, tk.END)
        self.entry_idLivroEmp.delete(0, tk.END)
        self.entry_dataEmprestimo.delete(0, tk.END)
        self.entry_dataPrevista.delete(0, tk.END)

    def devolver_livro(self):

        id_emprestimo = self.entry_idEmprestimoDev.get()

        resultado = self.emprestimo_controller.devolver(id_emprestimo)

        if resultado == "CAMPOS":
            messagebox.showerror("Erro", "Informe o ID do empréstimo!")
            return

        if resultado == "NAO_EXISTE":
            messagebox.showerror("Erro", "Empréstimo não encontrado!")
            return

        if resultado == "JA_DEVOLVIDO":
            messagebox.showerror("Erro", "Este empréstimo já foi devolvido!")
            return

        if resultado == "DEVOLVIDO":
            messagebox.showinfo("Sucesso", "Livro devolvido com sucesso!")
            self.entry_idEmprestimoDev.delete(0, tk.END)
            return

    def consultar_emprestimo(self):

        id_emprestimo = self.entry_consultaEmprestimo.get()

        if id_emprestimo == "":
            messagebox.showerror("Erro", "Informe o ID do empréstimo!")
            return

        resultado = self.emprestimo_controller.consultar(id_emprestimo)

        if resultado is None:
            messagebox.showerror("Erro", "Empréstimo não encontrado!")
            return

        status = "EM ABERTO"
        if resultado[7] is not None:
            status = "DEVOLVIDO"

        texto = (
            f"ID Empréstimo: {resultado[0]}\n"
            f"Matrícula: {resultado[1]}\n"
            f"Aluno: {resultado[2]}\n"
            f"ID Livro: {resultado[3]}\n"
            f"Título: {resultado[4]}\n"
            f"Data Empréstimo: {resultado[5]}\n"
            f"Data Prevista: {resultado[6]}\n"
            f"Data Devolução: {resultado[7]}\n"
            f"Status: {status}"
        )

        messagebox.showinfo("Consulta de Empréstimo", texto)

        self.entry_consultaEmprestimo.delete(0, tk.END)

    def criar_interface(self):

        titulo_principal = tk.Label(
            self.janela,
            text="📚 SISTEMA DE BIBLIOTECA",
            font=("Arial", 26, "bold"),
            fg="white",
            bg="#1e1e2e"
        )
        titulo_principal.pack(pady=20)

        self.menu_container = tk.Frame(self.frame_menu, bg="#1e1e2e")
        self.menu_container.pack(expand=True)

        self.frame_menu.pack(fill="both", expand=True)

        self.criar_botao_menu("👨‍🎓 Cadastrar Alunos", self.abrir_aluno).pack(pady=10)
        self.criar_botao_menu("📖 Cadastrar Livros", self.abrir_livro).pack(pady=10)
        self.criar_botao_menu("📌 Realizar Empréstimos", self.abrir_emprestimo).pack(pady=10)
        self.criar_botao_menu("🔄 Devolver Livros", self.abrir_devolucao).pack(pady=10)
        self.criar_botao_menu("🔍 Consultar Empréstimos", self.abrir_consulta).pack(pady=10)

        tk.Label(self.frame_aluno, text="Cadastro de Alunos", font=("Arial", 22, "bold"), fg="white", bg="#1e1e2e").pack(pady=20)

        tk.Label(self.frame_aluno, text="Nome:", font=("Arial", 14), fg="white", bg="#1e1e2e").pack(pady=5)
        self.entry_nome = tk.Entry(self.frame_aluno, font=("Arial", 14), width=30)
        self.entry_nome.pack(pady=5)

        tk.Label(self.frame_aluno, text="Curso:", font=("Arial", 14), fg="white", bg="#1e1e2e").pack(pady=5)
        self.entry_curso = tk.Entry(self.frame_aluno, font=("Arial", 14), width=30)
        self.entry_curso.pack(pady=5)

        tk.Label(self.frame_aluno, text="Matrícula:", font=("Arial", 14), fg="white", bg="#1e1e2e").pack(pady=5)
        self.entry_matricula = tk.Entry(self.frame_aluno, font=("Arial", 14), width=30)
        self.entry_matricula.pack(pady=5)

        tk.Button(self.frame_aluno, text="Salvar Aluno", font=("Arial", 16, "bold"), bg="#4a90e2", fg="white", width=20, command=self.salvar_aluno).pack(pady=20)
        tk.Button(self.frame_aluno, text="Voltar ao Menu", font=("Arial", 14), bg="#444", fg="white", width=20, command=self.voltar_menu).pack(pady=10)

        tk.Label(self.frame_livro, text="Cadastro de Livros", font=("Arial", 22, "bold"), fg="white", bg="#1e1e2e").pack(pady=20)

        tk.Label(self.frame_livro, text="Título do Livro:", font=("Arial", 14), fg="white", bg="#1e1e2e").pack(pady=5)
        self.entry_nomeLivro = tk.Entry(self.frame_livro, font=("Arial", 14), width=30)
        self.entry_nomeLivro.pack(pady=5)

        tk.Label(self.frame_livro, text="Autor:", font=("Arial", 14), fg="white", bg="#1e1e2e").pack(pady=5)
        self.entry_nomeAutor = tk.Entry(self.frame_livro, font=("Arial", 14), width=30)
        self.entry_nomeAutor.pack(pady=5)

        tk.Label(self.frame_livro, text="Quantidade:", font=("Arial", 14), fg="white", bg="#1e1e2e").pack(pady=5)
        self.entry_quantidadeLivro = tk.Entry(self.frame_livro, font=("Arial", 14), width=30)
        self.entry_quantidadeLivro.pack(pady=5)

        tk.Label(self.frame_livro, text="ID do Livro:", font=("Arial", 14), fg="white", bg="#1e1e2e").pack(pady=5)
        self.entry_idLivro = tk.Entry(self.frame_livro, font=("Arial", 14), width=30)
        self.entry_idLivro.pack(pady=5)

        tk.Button(self.frame_livro, text="Salvar Livro", font=("Arial", 16, "bold"), bg="#4a90e2", fg="white", width=20, command=self.salvar_livro).pack(pady=20)
        tk.Button(self.frame_livro, text="Voltar ao Menu", font=("Arial", 14), bg="#444", fg="white", width=20, command=self.voltar_menu).pack(pady=10)

        tk.Label(self.frame_emprestimo, text="Realizar Empréstimos", font=("Arial", 22, "bold"), fg="white", bg="#1e1e2e").pack(pady=15)

        tk.Label(self.frame_emprestimo, text="ID do empréstimo", font=("Arial", 14), fg="white", bg="#1e1e2e").pack(pady=2)
        self.entry_idEmprestimo = tk.Entry(self.frame_emprestimo, font=("Arial", 14), width=30)
        self.entry_idEmprestimo.pack(pady=5)

        tk.Label(self.frame_emprestimo, text="Matrícula do aluno", font=("Arial", 14), fg="white", bg="#1e1e2e").pack(pady=2)
        self.entry_matriculaAluno = tk.Entry(self.frame_emprestimo, font=("Arial", 14), width=30)
        self.entry_matriculaAluno.pack(pady=5)

        tk.Label(self.frame_emprestimo, text="ID do livro", font=("Arial", 14), fg="white", bg="#1e1e2e").pack(pady=2)
        self.entry_idLivroEmp = tk.Entry(self.frame_emprestimo, font=("Arial", 14), width=30)
        self.entry_idLivroEmp.pack(pady=5)

        tk.Label(self.frame_emprestimo, text="Data do empréstimo (AAAA-MM-DD)", font=("Arial", 14), fg="white", bg="#1e1e2e").pack(pady=2)
        self.entry_dataEmprestimo = tk.Entry(self.frame_emprestimo, font=("Arial", 14), width=30)
        self.entry_dataEmprestimo.pack(pady=5)

        tk.Label(self.frame_emprestimo, text="Data prevista devolução (AAAA-MM-DD)", font=("Arial", 14), fg="white", bg="#1e1e2e").pack(pady=2)
        self.entry_dataPrevista = tk.Entry(self.frame_emprestimo, font=("Arial", 14), width=30)
        self.entry_dataPrevista.pack(pady=5)

        tk.Button(self.frame_emprestimo, text="Realizar Empréstimo", font=("Arial", 16, "bold"), bg="#4a90e2", fg="white", width=25, command=self.realizar_emprestimo).pack(pady=15)
        tk.Button(self.frame_emprestimo, text="Voltar ao Menu", font=("Arial", 14), bg="#444", fg="white", width=20, command=self.voltar_menu).pack(pady=15)

        tk.Label(self.frame_devolucao, text="Devolver Livro", font=("Arial", 22, "bold"), fg="white", bg="#1e1e2e").pack(pady=20)

        tk.Label(self.frame_devolucao, text="ID do Empréstimo:", font=("Arial", 14), fg="white", bg="#1e1e2e").pack(pady=5)
        self.entry_idEmprestimoDev = tk.Entry(self.frame_devolucao, font=("Arial", 14), width=30)
        self.entry_idEmprestimoDev.pack(pady=5)

        tk.Button(self.frame_devolucao, text="Confirmar Devolução", font=("Arial", 16, "bold"), bg="#4a90e2", fg="white", width=25, command=self.devolver_livro).pack(pady=20)
        tk.Button(self.frame_devolucao, text="Voltar ao Menu", font=("Arial", 14), bg="#444", fg="white", width=20, command=self.voltar_menu).pack(pady=10)

        tk.Label(self.frame_consulta, text="Consultar Empréstimo", font=("Arial", 22, "bold"), fg="white", bg="#1e1e2e").pack(pady=20)

        tk.Label(self.frame_consulta, text="ID do Empréstimo:", font=("Arial", 14), fg="white", bg="#1e1e2e").pack(pady=5)
        self.entry_consultaEmprestimo = tk.Entry(self.frame_consulta, font=("Arial", 14), width=30)
        self.entry_consultaEmprestimo.pack(pady=5)

        tk.Button(self.frame_consulta, text="Consultar", font=("Arial", 16, "bold"), bg="#4a90e2", fg="white", width=20, command=self.consultar_emprestimo).pack(pady=20)
        tk.Button(self.frame_consulta, text="Voltar ao Menu", font=("Arial", 14), bg="#444", fg="white", width=20, command=self.voltar_menu).pack(pady=10)

        rodape = tk.Label(self.janela, text="Desenvolvido em Python + Tkinter", font=("Arial", 12), fg="white", bg="#1e1e2e")
        rodape.pack(side="bottom", pady=20)

    def iniciar(self):
        self.janela.mainloop()
