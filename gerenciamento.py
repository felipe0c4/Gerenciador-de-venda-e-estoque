from tkinter import *
from databaseprodutos import produtos
from databasevendas import vendasDB

def realizar_venda():
    itemv = item.get()
    quantidadev = int(quantidade.get())
    atual_item = -1
    for item_auth in produtos:
        atual_item += 1
        if item_auth["item"] == itemv:
            if item_auth["quantidade"] >= quantidadev:
                if item_auth["quantidade"] == 0:
                    erro2["text"] = "Produto Indisponivel"
                else:
                    item_vendido = item_auth["item"]
                    preco = item_auth["preço"]
                    print(f"item_vendido: {item_vendido}")
                    vendasDB.append(
                        {"item": item_vendido, "preço": preco, "quantidade": quantidadev}
                    )
                    produtos[atual_item]["quantidade"] = item_auth["quantidade"] - quantidadev
                    gerenc.destroy()
                    venda.destroy()
                    print(vendasDB)
                    print(produtos)
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

    for prod in produtos:
        Label(gerenc, text=prod["item"]).place(relx=0.27, rely=ycount, anchor=CENTER)
        Label(gerenc, text=prod["preço"]).place(relx=0.47, rely=ycount, anchor=CENTER)
        Label(gerenc, text=prod["quantidade"]).place(relx=0.67, rely=ycount, anchor=CENTER)
        ycount += 0.1


    Button(gerenc, text="Realizar Venda", command=painel_vendas).place(relx=0.5, rely=ycount+1, anchor=CENTER)


    gerenc.mainloop()
