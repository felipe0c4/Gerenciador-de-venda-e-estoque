from tkinter import *
import peewee

import gerenciamento
from database import Logins
from gerenciamento import *

def auth():
    userconteudo = user.get()
    senhaconteudo = senha.get()
    for user_auth in Logins:
        if user_auth["usuario"] == userconteudo and user_auth["senha"] == senhaconteudo:
            print(f'usuario {user_auth["usuario"]}, senha {user_auth["senha"]}')
            login.destroy()
            gerenciamento.gerenc_interface()
        else:
            a['text'] = "credenciais invalidas"


login = Tk()

Label(login, text="Login").pack()
user = Entry(login)
user.pack()

Label(login, text="Senha").pack()
senha = Entry(login)
senha.pack()

a = Label(login, text='')
a.pack()

Button(login, text="Click me", command=auth).pack()

login.mainloop()
