from tkinter import *
from tkinter import ttk

class AddPessoas:
    def __init__(self, master):
        self.master = master
        self.frameCampo = Frame(self.master)
        self.frameCampo.pack()

        self.frameBtn = Frame(self.master)
        self.frameBtn.pack()

    def campos(self):
        Label(self.frameCampo, text="Nome Completo", font="Montserrat").grid(row=0, column=0)
        nome  = Entry(self.frameCampo, width=100, font="Montserrat").grid(row=1, column=0, columnspan=4)

        Label(self.frameCampo, text="CPF", font="Montserrat").grid(row=2, column=0)
        CPF  = Entry(self.frameCampo, width=50, font="Montserrat").grid(row=3, column=0, columnspan=2)

        Label(self.frameCampo, text="Telefone", font="Montserrat").grid(row=2, column=2)
        telefone  = Entry(self.frameCampo, width=50, font="Montserrat").grid(row=3, column=2, columnspan=2)

        Label(self.frameCampo, text="E-mail", font="Montserrat").grid(row=4, column=0)
        email  = Entry(self.frameCampo, width=100, font="Montserrat").grid(row=5, column=0, columnspan=4)

        Label(self.frameCampo, text="Endetereço", font="Montserrat").grid(row=6, column=0)
        endereco  = Text(self.frameCampo, height=5, width=100, font="Montserrat").grid(row=7, column=0, columnspan=4)

        Label(self.frameCampo, text="Login", font="Montserrat").grid(row=8, column=0)
        login  = Entry(self.frameCampo, width=20, font="Montserrat").grid(row=9, column=0)

        Label(self.frameCampo, text="Senha", font="Montserrat").grid(row=8, column=1)
        senha  = Entry(self.frameCampo, width=20, font="Montserrat").grid(row=9, column=1)

        Label(self.frameCampo, text="Repita sua Senha", font="Montserrat").grid(row=8, column=2)
        rpSenha  = Entry(self.frameCampo, width=20, font="Montserrat").grid(row=9, column=2)

        Label(self.frameCampo, text="Tipo de Pessoa", font="Montserrat").grid(row=8, column=3)
        tipo = ttk.Combobox(self.frameCampo, width=20, font="Montserrat")
        tipo.grid(row=9, column=3)
        tipo['value'] = ["Cliente", "Funcionario", "Gerente"]
        tipo.current(1)

    def butao(self):
        btn = Button(self.frameBtn, text="Salvar", font="Montserrat")
        btn.pack(pady=20)
