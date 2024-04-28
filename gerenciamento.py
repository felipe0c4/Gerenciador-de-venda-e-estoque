from tkinter import *
from database import Produtos, Vendas

def realizar_venda():
    itemv = item.get()
    quantidadev = int(quantidade.get())
    atual_item = -1
    for item_auth in Produtos.select():
        atual_item += 1
        if item_auth.item == itemv:
            if item_auth.quantidade >= quantidadev:
                if item_auth.quantidade == 0:
                    erro2["text"] = "Produto Indisponivel"
                else:
                    item_auth.quantidade = item_auth.quantidade - quantidadev
                    item_auth.save()
                    Vendas.create(item=item_auth.item, preco=item_auth.preco, quantidade=quantidadev)
                    gerenc.destroy()
                    venda.destroy()
                    gerenc_interface()
            else:
                erro2["text"] = "Quantidade invalida"
        else:
            erro["text"] = "Produto não encontrado"


def painel_vendas():
    global item, quantidade, erro, erro2, venda
    venda = Tk()
    item = Entry(venda)
    item.grid(column=0, row=1)
    quantidade = Entry(venda)
    quantidade.grid(column=1, row=1)
    erro = Label(venda, text="")
    erro2 = Label(venda, text="")
    erro.grid(column=0, row=3)
    erro2.grid(column=1, row=3)

    Label(venda, text="Produto").grid(column=0, row=0)
    Label(venda, text="Quantidade").grid(column=1, row=0)
    Button(venda, text="Atribuir Venda", command=realizar_venda).grid(column=3, row=1)

    venda.mainloop()

def Historico():
    historico = Tk()

    ycount = 0.1

    for prod in Vendas.select():
        Label(historico, text=prod.item).place(relx=0.27, rely=ycount, anchor=CENTER)
        Label(historico, text=prod.preco).place(relx=0.47, rely=ycount, anchor=CENTER)
        Label(historico, text=prod.quantidade).place(relx=0.67, rely=ycount, anchor=CENTER)
        ycount += 0.1

    historico.mainloop()

def gerenc_interface():
    global gerenc
    gerenc = Tk()
    gerenc.title("Gerenciamento")
    gerenc.geometry("500x300")
    ycount = 0.4
    label_produtos = Label(gerenc, text="Produtos: ")
    label_produtos.place(relx=0.27, rely=0.3, anchor=CENTER)

    label_precos = Label(gerenc, text="Preços: ")
    label_precos.place(relx=0.47, rely=0.3, anchor=CENTER)

    label_quantidade = Label(gerenc, text="Quantidade: ")
    label_quantidade.place(relx=0.67, rely=0.3, anchor=CENTER)

    Button(gerenc, text="Realizar Venda", command=painel_vendas).pack()
    Button(gerenc, text="Historico de Vendas", command=Historico).pack()

    for prod in Produtos.select():
        Label(gerenc, text=prod.item).place(relx=0.27, rely=ycount, anchor=CENTER)
        Label(gerenc, text=prod.preco).place(relx=0.47, rely=ycount, anchor=CENTER)
        Label(gerenc, text=prod.quantidade).place(relx=0.67, rely=ycount, anchor=CENTER)
        ycount += 0.1

    gerenc.mainloop()
