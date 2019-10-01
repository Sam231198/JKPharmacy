from tkinter import *
from tkinter import ttk
from db.connectSQLite import *


class AddPessoas:
    def __init__(self, master):
        self.master = master
        self.frameCampo = Frame(self.master)
        self.frameCampo.pack()

        self.frameBtn = Frame(self.master)
        self.frameBtn.pack()

    def campos(self):
        Label(self.frameCampo, text="Nome Completo", font="Montserrat").grid(row=0, column=0)
        self.nome = Entry(self.frameCampo, width=100, font="Montserrat")
        self.nome.grid(row=1, column=0, columnspan=4)

        Label(self.frameCampo, text="CPF", font="Montserrat").grid(row=2, column=0)
        self.CPF = Entry(self.frameCampo, width=50, font="Montserrat")
        self.CPF.grid(row=3, column=0, columnspan=2)

        Label(self.frameCampo, text="Telefone", font="Montserrat").grid(row=2, column=2)
        self.telefone = Entry(self.frameCampo, width=50, font="Montserrat")
        self.telefone.grid(row=3, column=2, columnspan=2)

        Label(self.frameCampo, text="E-mail", font="Montserrat").grid(row=4, column=0)
        self.email = Entry(self.frameCampo, width=100, font="Montserrat")
        self.email.grid(row=5, column=0, columnspan=4)

        Label(self.frameCampo, text="Endetereço", font="Montserrat").grid(row=6, column=0)
        self.endereco = Text(self.frameCampo, height=5, width=100, font="Montserrat")
        self.endereco.grid(row=7, column=0, columnspan=4)

        Label(self.frameCampo, text="Login", font="Montserrat").grid(row=8, column=0)
        self.login = Entry(self.frameCampo, width=20, font="Montserrat")
        self.login.grid(row=9, column=0)

        Label(self.frameCampo, text="Senha", font="Montserrat").grid(row=8, column=1)
        self.senha = Entry(self.frameCampo, width=20, font="Montserrat")
        self.senha.grid(row=9, column=1)

        Label(self.frameCampo, text="Repita sua Senha", font="Montserrat").grid(row=8, column=2)
        self.rpSenha = Entry(self.frameCampo, width=20, font="Montserrat")
        self.rpSenha.grid(row=9, column=2)

        Label(self.frameCampo, text="Tipo de Pessoa", font="Montserrat").grid(row=8, column=3)
        self.tipo = ttk.Combobox(self.frameCampo, width=20, font="Montserrat")
        self.tipo.grid(row=9, column=3)
        self.tipo['value'] = ["Cliente", "Funcionario", "Gerente"]
        self.tipo.current(1)

    def butao(self):
        btn = Button(self.frameBtn, text="Salvar", font="Montserrat", command=self.cadastrar)
        btn.pack(pady=20)

    def cadastrar(self):

        nome = self.nome.get()
        cpf = self.CPF.get()
        email = self.email.get()
        telefone = self.telefone.get()
        endereco = self.endereco.get(1.0, END)
        login = self.login.get()
        cargo = self.tipo.get()
        senha = self.rpSenha.get()

        if cargo == "Cliente":
            cursor.execute("INSERT INTO cliente(nome,"
                           "cpf,"
                           "email,"
                           "telefone,"
                           "endereco)"
                           " VALUES({nome},"
                           "{cpf},"
                           "{email},"
                           "{telefone},"
                           "{endereco})"
                           .format(nome=nome,
                                   cpf=cpf,
                                   email=email,
                                   telefone=telefone,
                                   endereco=endereco))
        else:
            cursor.execute("INSERT INTO funcionario(nome,"
                           "cpf,"
                           "email,"
                           "telefone,"
                           "endereco,"
                           "login,"
                           "cargo,"
                           "senha)"
                           " VALUES "
                           "({nome},"
                           "{cpf},"
                           "{email},"
                           "{telefone},"
                           "{endereco},"
                           "{login},"
                           "{cargo},"
                           "{senha})"
                           .format(nome=nome,
                           cpf=cpf,
                           email=email,
                           telefone=telefone,
                           endereco=endereco,
                           login=login,
                           cargo=cargo,
                           senha=senha))
            sqlite.commit()

