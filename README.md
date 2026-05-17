![Python](https://img.shields.io/badge/Python-3-blue)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)
![MVC](https://img.shields.io/badge/Architecture-MVC-green)
![Status](https://img.shields.io/badge/Status-Finalizado-success)

# Sistema de Biblioteca 📚

Sistema de gerenciamento de biblioteca desenvolvido em Python utilizando Programação Orientada a Objetos (POO), arquitetura MVC, interface gráfica com Tkinter e integração com banco de dados MySQL.

---

## 🚀 Funcionalidades

- Cadastro de alunos
- Cadastro de livros
- Sistema de empréstimos
- Atualização e remoção de registros
- Interface gráfica com Tkinter
- Integração com banco de dados MySQL
- Organização em padrão MVC
- Código estruturado com POO

---

## 🛠 Tecnologias Utilizadas

- Python 3
- Tkinter
- MySQL
- MySQL Connector
- POO (Programação Orientada a Objetos)
- MVC (Model View Controller)

---

## 📂 Estrutura do Projeto

```bash
📦 sistema-biblioteca-mvc
 ┣ 📂 controller
 ┃ ┣ 📜 aluno_controller.py
 ┃ ┣ 📜 livro_controller.py
 ┃ ┗ 📜 emprestimo_controller.py
 ┃
 ┣ 📂 model
 ┃ ┣ 📜 aluno.py
 ┃ ┣ 📜 livro.py
 ┃ ┗ 📜 emprestimo.py
 ┃
 ┣ 📂 view
 ┃ ┣ 📜 tela_alunos.py
 ┃ ┣ 📜 tela_livros.py
 ┃ ┗ 📜 tela_emprestimos.py
 ┃
 ┣ 📂 database
 ┃ ┗ 📜 conexao.py
 ┃
 ┣ 📜 main.py
 ┗ 📜 README.md
```
---

## ⚙️ Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/joaonass/sistema-biblioteca-mvc
```

---

### 2. Acesse a pasta

```bash
cd sistema-biblioteca-mvc
```

---

### 3. Instale as dependências

```bash
pip install mysql-connector-python
```

---

### 4. Configure o banco de dados

Crie um banco MySQL e configure as credenciais no arquivo:

```python
database/conexao.py
```

Exemplo:

```python
host="localhost"
user="root"
password="SUA_SENHA"
database="biblioteca"
```

---

## 🗄 Estrutura do Banco de Dados

### Tabela: alunos

| Campo | Tipo |
|---|---|
| id_aluno | INT |
| nome | VARCHAR |
| curso | VARCHAR |
| matricula | VARCHAR |

---

### Tabela: livros

| Campo | Tipo |
|---|---|
| id_livro | INT |
| titulo | VARCHAR |
| autor | VARCHAR |
| quantidade | INT |

---

### Tabela: emprestimos

| Campo | Tipo |
|---|---|
| id_emprestimo | INT |
| id_aluno | INT |
| id_livro | INT |
| data_emprestimo | VARCHAR |
| data_devolucao | VARCHAR |

---

## 🧠 Conceitos Aplicados

### 🔹 Programação Orientada a Objetos

O projeto utiliza encapsulamento, classes, atributos privados, métodos getters/setters e separação de responsabilidades.

---

### 🔹 Arquitetura MVC

- **Model:** responsável pelos dados e regras de negócio.
- **View:** interface gráfica e interação com usuário.
- **Controller:** faz a comunicação entre View e Model.

---

## 📸 Interface

O sistema possui interface gráfica desenvolvida com Tkinter para facilitar o gerenciamento da biblioteca.

<img width="1495" height="908" alt="image" src="https://github.com/user-attachments/assets/f6970312-88b1-4f94-92e1-94dab5836b44" />

---

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido com objetivo de praticar:

- Python avançado
- Organização profissional de código
- Arquitetura MVC
- Integração com banco de dados
- Desenvolvimento de sistemas desktop

---

## 👨‍💻 Autor

Desenvolvido por João Nass.
