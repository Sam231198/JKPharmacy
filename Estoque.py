from tkinter import *
from tkinter import ttk


class Estoque:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()

        self.frameProdutos = Frame(self.frame)
        self.frameProdutos.grid(row=0, column=0, pady=10)

        self.frameNewProdutos = Frame(self.frame)
        self.frameNewProdutos.grid(row=0, column=1, padx=5)

    def pequisaproduto(self):
        frame = Frame(self.frameProdutos)
        frame.pack(expand=True, pady=5)
        Label(frame, text="Pesq.", font="Montserrat").grid(row=0, column=0)
        pesquisa = Entry(frame, width=45, font="Montserrat").grid(row=0, column=1)

    def tabela(self):
        tabela = ttk.Treeview(self.frameProdutos, columns=('Produto', 'Qtd','Preço'))
        tabela.pack()
        tabela.heading('#0', text='Id_Produto')
        tabela.column("#0", minwidth=70, width=70, stretch=NO)

        tabela.heading('#1', text='Produto')
        tabela.column("#1", minwidth=70, stretch=NO)

        tabela.heading('#2', text='Qtd')
        tabela.column("#2", minwidth=70, width=70, stretch=NO)

        tabela.heading('#3', text='Preço')
        tabela.column("#3", minwidth=70, stretch=NO)

    def newProduto(self):
        label_frame = LabelFrame(self.frameNewProdutos, text='Novo Produto', font="Montserrat", padx=5, pady=5)
        label_frame.pack(expand=True)

        Label(label_frame, text="Nome do Produto", font="Montserrat").grid(row=0, column=0, pady=5)
        nomeProduto = Entry(label_frame, width=35, font="Montserrat").grid(row=0, column=1, padx=5, pady=10)

        Label(label_frame, text="Marca", font="Montserrat").grid(row=1, column=0, pady=5)
        marca = Entry(label_frame, width=35, font="Montserrat").grid(row=1, column=1, padx=5, pady=10)

        Label(label_frame, text="Validade", font="Montserrat").grid(row=2, column=0, pady=5)
        validade = Entry(label_frame, width=35, font="Montserrat").grid(row=2, column=1, pady=10)

        Label(label_frame, text="Qtd", font="Montserrat").grid(row=3, column=0, pady=5)
        quantidade = Entry(label_frame, width=35, font="Montserrat").grid(row=3, column=1, pady=10)

        Label(label_frame, text="Preço", font="Montserrat").grid(row=4, column=0, pady=5)
        preco = Entry(label_frame, width=35, font="Montserrat").grid(row=4, column=1, pady=10)

        # Label(label_frame, text="Tipo").grid(row=5, column=0)
        # tipo = ttk.Combobox(label_frame)
        # tipo.grid(row=5, column=1)
        # tipo['value'] = ["1", "10", "11", "100"]
        # tipo.current(1)

        bntAdd = Button(label_frame,text="✚", font="Montserrat").grid(row=5, column=1)



    def atualizacaoEstoque(self):
        frame = Frame(self.frameProdutos)
        frame.pack()

        Label(frame, text="Cod.", font="Montserrat").grid(row=0, column=0)
        cod = Entry(frame).grid(row=0, column=1)

        Label(frame, text="Qtd.", font="Montserrat").grid(row=0, column=2)
        qtd = Entry(frame).grid(row=0, column=3)

        btdAdd = Button(frame, text="✚", font="Montserrat 6")
        btdAdd.grid(row=0, column=4, padx=5)
        btdRemover = Button(frame, text="✖", font="Montserrat 6")
        btdRemover.grid(row=0, column=5, padx=5)
