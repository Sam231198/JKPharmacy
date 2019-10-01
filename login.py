from tkinter import *
root = Tk()
root.title("JK Pharmacy")

# logo do aplicativo
logoImg = PhotoImage(file="img/logo.png")
logoLabel = Label(root, image=logoImg)
logoLabel.pack()

# conteiner dos campos de login e senha
frameLogin = Frame(root, width=768, height=576)
frameLogin.pack()

# campo de login
loginLabel = Label(frameLogin, text="Login", font="Montserrat")
loginLabel.grid(row=0, column=0, padx=5, pady=5)

loginEntry = Entry(frameLogin, font="Montserrat")
loginEntry.grid(row=0, column=1, padx=5, pady=5)

# campo de senha
senhaLabel = Label(frameLogin, text="Senha", font="Montserrat")
senhaLabel.grid(row=1, column=0, padx=5, pady=5)

senhaEntry = Entry(frameLogin, font="Montserrat", show='●')
senhaEntry.grid(row=1, column=1, padx=5, pady=5)

# butão de login
loginBtn = Button(frameLogin, text="Logar", font="Montserrat", width=15)
loginBtn.grid(row=2, columnspan=2, padx=5, pady=5)


root.geometry("400x210")
root.resizable(width=False, height=False)
root.minsize(width=400, height=350)
root.maxsize(width=400, height=350)
root.mainloop()
