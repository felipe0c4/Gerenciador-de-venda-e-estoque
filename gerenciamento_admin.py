from tkinter import *
from database import Produtos

def adicionando():
    pdt = add_produto.get()
    prc = float(add_preco.get())
    qtd = int(add_quantidade.get())
    for item_auth in Produtos.select():
        if item_auth.item == pdt:
            item_auth.preco = prc
            item_auth.quantidade += qtd
            item_auth.save()
            break
    else:
        Produtos.create(item=pdt, preco=prc, quantidade=qtd)

    gerenc.destroy()
    add.destroy()
    gerenc_interface_admin()

def remover():
    pdt = delete_produto.get()
    for item_auth in Produtos.select():
        if item_auth.item == pdt:
            item_auth.delete_instance()
            break
    else:
        err["text"] = "Produto não encontrado"

    gerenc.destroy()
    deletar.destroy()
    gerenc_interface_admin()

def deletar_item():

    global delete_produto, err, deletar
    deletar = Tk()
    err = Label(deletar, text="")
    err.grid()
    Label(deletar, text="Delete os Itens").grid()
    delete_produto = Entry(deletar)
    delete_produto.grid()
    Button(deletar, text="Delete", command=remover).grid()

    deletar.mainloop()

def adicionar_item():
    global add_produto, add_preco, add_quantidade, add
    add = Tk()
    add.geometry("500x200")
    add_produto = Entry(add)
    add_preco = Entry(add)
    add_quantidade = Entry(add)
    add_produto.place(relx=0.17, rely=0.3, anchor=CENTER)
    add_preco.place(relx=0.47, rely=0.3, anchor=CENTER)
    add_quantidade.place(relx=0.77, rely=0.3, anchor=CENTER)


    Label(add, text="Produto").place(relx=0.17, rely=0.1, anchor=CENTER)
    Label(add, text="Preço").place(relx=0.47, rely=0.1, anchor=CENTER)
    Label(add, text="Quantidade").place(relx=0.77, rely=0.1, anchor=CENTER)
    Button(add, text="Adicionar", command=adicionando).place(relx=0.5, rely=0.6, anchor=CENTER)




def gerenc_interface_admin():
    global gerenc
    gerenc = Tk()
    gerenc.geometry("500x300")
    gerenc.title("Painel Admin")
    Label(gerenc, text="Gerenciamento de Estoque").grid()
    Button(gerenc, text="Adicionar Itens", command=adicionar_item).grid()
    Button(gerenc, text="Deletar Itens", command=deletar_item).grid()

    ycount = 0.4

    label_produtos = Label(gerenc, text="Produtos: ")
    label_produtos.place(relx=0.27, rely=0.3, anchor=CENTER)

    label_precos = Label(gerenc, text="Preços: ")
    label_precos.place(relx=0.47, rely=0.3, anchor=CENTER)

    label_quantidade = Label(gerenc, text="Quantidade: ")
    label_quantidade.place(relx=0.67, rely=0.3, anchor=CENTER)

    for prod in Produtos.select():
        Label(gerenc, text=prod.item).place(relx=0.27, rely=ycount, anchor=CENTER)
        Label(gerenc, text=prod.preco).place(relx=0.47, rely=ycount, anchor=CENTER)
        Label(gerenc, text=prod.quantidade).place(relx=0.67, rely=ycount, anchor=CENTER)
        ycount += 0.1

    gerenc.mainloop()

