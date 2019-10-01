from tkinter import *
from tkinter import ttk

class Vendas:
    def __init__(self, master,):
        self.master = master

        self.frameCampos = Frame(self.master)
        self.frameCampos.pack()

        # fieldset do campo "Funcionario"
        self.legendFrameClientesFuncionario = LabelFrame(self.frameCampos, text='Funcionario', font="Montserrat", padx=5, pady=5)
        self.legendFrameClientesFuncionario.grid(row=0, column=0, padx=5)

        # fieldset do campo "Produto"
        self.legendFrameProdutos = LabelFrame(self.frameCampos, text='Produto', font="Montserrat", padx=5, pady=5)
        self.legendFrameProdutos.grid(row=0, column=1, columnspan=2, padx=5)

        self.frameCarinho = Frame(self.master)
        self.frameCarinho.pack(pady=5)

        self.frameButao = Frame(self.master)
        self.frameButao.pack(pady=5)

    def cliente(self):
        # campos para informa o cliente
        frame = Frame(self.legendFrameClientesFuncionario)
        frame.pack()

        # pesquisar por codigo do cliente
        Label(frame, text="Cód. Cliente", font="Montserrat").grid(row=0, column=0)
        entryCod = Entry(frame).grid(row=0, column=1)

        # pesquisar por nome do cliente
        Label(frame, text="Nome do Cliente", font="Montserrat").grid(row=0, column=2)
        entryNome = Entry(frame).grid(row=0, column=3)

    def funcionario(self):
        # campos para informa o vendedor
        frame = Frame(self.legendFrameClientesFuncionario)
        frame.pack()

        # pesquisar por codigo do cliente
        Label(frame, text="Cód. Vendedor", font="Montserrat").grid(row=0, column=0)
        entryCod = Entry(frame).grid(row=0, column=1)

        # pesquisar por nome do cliente
        Label(frame, text="Nome do Vendedor", font="Montserrat").grid(row=0, column=2)
        entryNome = Entry(frame).grid(row=0, column=3)

    def produtos(self):
        Label(self.legendFrameProdutos, text="Cód. Produto", font="Montserrat").grid(row=0, column=0)
        entryCod = Entry(self.legendFrameProdutos).grid(row=0, column=1)

        Label(self.legendFrameProdutos, text="Nome do Produto", font="Montserrat").grid(row=0, column=2)
        entryNome = Entry(self.legendFrameProdutos).grid(row=0, column=3)

        Label(self.legendFrameProdutos, text="Quantidade", font="Montserrat").grid(row=1, column=0)
        entryQnt = Entry(self.legendFrameProdutos).grid(row=1, column=1)

        labelPreco = Label(self.legendFrameProdutos, text="Preço: 0,00", font="Montserrat").grid(row=1, column=2)

        btnAdicionar = Button(self.legendFrameProdutos, text="✚", font="Montserrat").grid(row=0, column=4, rowspan=2, padx=5)

    def tabela(self):
        carinho = ttk.Treeview(self.frameCarinho, columns=('Produto', 'Preço', 'Desconto','Total'), height=20)
        carinho.pack()
        carinho.heading('#0', text='Id_Produto')
        carinho.heading('#1', text='Produto')
        carinho.heading('#2', text='Preço')
        carinho.heading('#3', text='Desconto')
        carinho.heading('#4', text='Total')

    def butao(self):
        # btnAdd = Button(self.frameButao, text="Adicionar")
        # btnAdd.grid(row=0, column=0, padx=20)
        btnFinalizar = Button(self.frameButao, text="Finalizar", font="Montserrat")
        btnFinalizar.pack()
