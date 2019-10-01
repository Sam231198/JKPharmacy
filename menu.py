from tkinter import *
from tkinter import ttk
from Perfil import Perfil
from Vendas import Vendas
from Estoque import Estoque
from AddPessoas import AddPessoas

root = Tk()
root.title("JK Pharmacy")

# declaração do menu suspenso
menu = ttk.Notebook(root)

# frame e definição de conteudo do perfil
framePerfil = Frame(menu)
foto = PhotoImage(file="img/perfilUser.png")
perfil = Perfil(framePerfil)
perfil.perfil(foto)
perfil.dados()

# frame e definição de conteudo de vendas
frameVendas = Frame(menu)
vendas = Vendas(frameVendas)
vendas.cliente()
vendas.funcionario()
vendas.produtos()
vendas.butao()
vendas.tabela()

frameEstoque = Frame(menu)
estoque = Estoque(frameEstoque)
estoque.pequisaproduto()
estoque.newProduto()
estoque.tabela()
estoque.atualizacaoEstoque()

addPessoa = Frame(menu)
pessoa = AddPessoas(addPessoa)
pessoa.campos()
pessoa.butao()


perfilImg = PhotoImage(file="img/perfil.png")
vendasImg = PhotoImage(file="img/vendas.png")
cadastroImg = PhotoImage(file="img/cadastro.png")
depositoImg = PhotoImage(file="img/deposito.png")

menu.add(framePerfil, image=perfilImg)
menu.add(frameVendas, image=vendasImg)
menu.add(frameEstoque, image=depositoImg)
menu.add(addPessoa, image=cadastroImg)

menu.pack()

root.geometry("1000x700")
root.minsize(width=1150, height=650)
root.maxsize(width=1150, height=650)
root.mainloop()