import gerenciamento
import gerenciamento_admin
from gerenciamento_admin import *
from database import Login

Login.create(usuario="admin", senha="admin", admin=True)


Login.create(usuario="caixa", senha="caixa", admin=False)


def auth():
    userconteudo = user.get()
    senhaconteudo = senha.get()
    for user_auth in Login.select():
        if user_auth.usuario == userconteudo and user_auth.senha == senhaconteudo:
            login.destroy()
            if user_auth.admin:
                gerenciamento_admin.gerenc_interface_admin()
            else:
                gerenciamento.gerenc_interface()
        else:
            a['text'] = "credenciais invalidas"


login = Tk()
login.title("Login")
login.geometry("300x150")

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

