from tkinter import *
from databaseprodutos import produtos

def gerenc_interface():
    gerenc = Tk()

    Label(gerenc, text="Produtos:").grid(column=1, row=0)

    for prod in produtos:
        Label(gerenc, text=prod["item"])

    gerenc.mainloop()