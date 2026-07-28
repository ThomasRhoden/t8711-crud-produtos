import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()

janela.title("Meu primeiro sisteminha")
janela.geometry("800x600")
janela.resizable(False, False)

# --------------------------------------------

lbl_titulo = tk.Label(
    janela,
    text = "EXEMPLO DE CADASTRO",
    font = ("Arial", 12, "bold")
)

lbl_titulo.grid(
    row = 0,
    column = 0,
    padx = 10,
    pady = 5,
    columnspan = 3
)

# --------------------------------------------
# Label = lbl
# Nome
lbl_nome = tk.Label(
    janela,
    text = "Nome:"
)

lbl_nome.grid(
    row = 1,
    column = 0,
    padx = 10,
    pady = 5
)

# Entry = Recebe(lê)
txt_nome = tk.Entry(
    janela,
    width = 40 # 40 caracteres
)

txt_nome.grid(
    row = 1,
    column = 1
)
# --------------------------------------------
# Idade
lbl_idade = tk.Label(
    janela,
    text = "Idade"
)

lbl_idade.grid(
    row = 2,
    column = 0,
    padx = 10,
    pady = 5
)

txt_idade = tk.Entry(
    janela,
    width = 40
)

txt_idade.grid(
    row = 2,
    column = 1
)
# --------------------------------------------
# Button = btn
def printar():
    print(txt_nome.get())

btn_escrever_nome = tk.Button(
    janela,
    text = "Printar o nome",
    command = printar
)

btn_escrever_nome.grid(
    row = 3,
    column = 0,
    padx = 10,
    pady = 5
)

# --------------------------------------------
# Avaliar idade
def avaliar_idade():
    if txt_idade.get() == "":
        messagebox.showerror(
            "Sisteminha",
            "O campo está vazio!"
        )
        return    
    idade = int(txt_idade.get())
    if idade >= 18:
        messagebox.showinfo(
            "Sisteminha",
            "Com " + str(idade) + " você é bem vindo!"
        )
        return
    messagebox.showwarning(
        "Sisteminha",
        "Menor de idade!"
    )
    return

btn_avaliar_idade = tk.Button(
    janela,
    text = "Avaliar idade",
    command = avaliar_idade
)

btn_avaliar_idade.grid(
    row = 3,
    column = 1
)
# Init
janela.mainloop()