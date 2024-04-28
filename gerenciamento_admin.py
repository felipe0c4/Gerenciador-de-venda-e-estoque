from tkinter import *
from databaseprodutos import produtos


def adicionando():
    pdt = add_produto.get()
    prc = add_preco.get()
    qtd = int(add_quantidade.get())
    quantidade_de_produtos = -1
    forcount = -1

    for q in produtos:
        quantidade_de_produtos += 1

    for item_auth in produtos:
        if item_auth["item"] == pdt:
            item_auth["preço"] = prc
            item_auth["quantidade"] += qtd
            break
            print(produtos)
    else:
        produtos.append({"item": pdt, "preço": prc, "quantidade": qtd})
        print(produtos)
    gerenc.destroy()
    add.destroy()
    gerenc_interface_admin()

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

    ycount = 0.4

    label_produtos = Label(gerenc, text="Produtos: ")
    label_produtos.place(relx=0.27, rely=0.3, anchor=CENTER)

    label_precos = Label(gerenc, text="Preços: ")
    label_precos.place(relx=0.47, rely=0.3, anchor=CENTER)

    label_quantidade = Label(gerenc, text="Quantidade: ")
    label_quantidade.place(relx=0.67, rely=0.3, anchor=CENTER)

    for prod in produtos:
        Label(gerenc, text=prod["item"]).place(relx=0.27, rely=ycount, anchor=CENTER)
        Label(gerenc, text=prod["preço"]).place(relx=0.47, rely=ycount, anchor=CENTER)
        Label(gerenc, text=prod["quantidade"]).place(relx=0.67, rely=ycount, anchor=CENTER)
        ycount += 0.1

    gerenc.mainloop()
