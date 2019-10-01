from tkinter import *
class Perfil:
    def __init__(self, master):
        self.master = master

        self.frameDados = Frame(self.master)
        self.frameDados.grid(row=0, column=1)

    def perfil(self, foto):
        labelPerfil = Label(self.master, image=foto)
        labelPerfil.grid(row=0, column=0)

    def dados(self):
        labelNome = Label(self.frameDados, text="Samuel Marques Costa", font="Montserrat 30 bold")
        labelNome.pack()

        labelCargo = Label(self.frameDados, text="Dev Back-End", font="Montserrat 20")
        labelCargo.pack()

        labelCPF = Label(self.frameDados, text="000.000.000-00", font="Montserrat 15")
        labelCPF.pack()

        labelRG = Label(self.frameDados, text="0.000.000", font="Montserrat 15")
        labelRG.pack()

        labelEndereco = Label(self.frameDados, text="Qr 01 Lt 1, Pedregal - GO", font="Montserrat 15")
        labelEndereco.pack()

        labelTelefone = Label(self.frameDados, text="(61) 9 9564-5444", font="Montserrat 15")
        labelTelefone.pack()

        btnMudarSenha = Button(self.frameDados, text="Alterar Senha",font="Montserrat")
        btnMudarSenha.pack()

