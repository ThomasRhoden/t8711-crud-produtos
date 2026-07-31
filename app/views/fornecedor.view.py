import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from app.models.fornecedor import Fornecedor

import tkinter as tk
from tkinter import messagebox


class Fornecedor_View:
    def __init__(self, root):
        self.root = root
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title("CRUD de Fornecedores")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
  

    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text = "Cadastro de Fornecedores",
            font = ("Arial", 16, "bold"),
        )
        self.lbl_titulo.grid(
            row = 0,
            column = 0,
            columnspan = 4,
            padx = 5,
            pady = 5
        )
        self.frm_dados = tk.LabelFrame(
            self.root,
            text = "Dados do fornecedor"
        )
        self.frm_dados.grid(
            row = 1,
            column = 0,
            columnspan=4,
            padx = 10,
            pady = 5,
            sticky = "w"
        )
        self.lbl_id = tk.Label(
            self.frm_dados,
            text = "ID:"
        )
        self.lbl_id.grid(
            row = 0,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_id = tk.Entry(
            self.frm_dados,
            width = 10,
            state = "readonly"
        )
        self.txt_id.grid(
            row = 0,
            column= 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_razao_social = tk.Label(
            self.frm_dados,
            text = "Razão social:"
        )
        self.lbl_razao_social.grid(
            row = 1,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_razao_social = tk.Entry(
            self.frm_dados,
            width = 40
        )
        self.txt_razao_social.grid(
            row = 1,
            column = 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_nome_fantasia = tk.Label(
            self.frm_dados,
            text = "Nome fantasia:"
        )
        self.lbl_nome_fantasia.grid(
            row = 1,
            column = 2,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_nome_fantasia = tk.Entry(
            self.frm_dados,
            width = 40
        )
        self.txt_nome_fantasia.grid(
            row = 1,
            column = 3,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_cnpj = tk.Label(
            self.frm_dados,
            text = "CNPJ:"
        )
        self.lbl_cnpj.grid(
            row = 2,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_cnpj = tk.Entry(
            self.frm_dados,
            width = 20
        )
        self.txt_cnpj.grid(
            row = 2,
            column = 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_sla = tk.Label(
            self.frm_dados,
            text = "SLA de atendimento:"
        )
        self.lbl_sla.grid(
            row = 2,
            column = 2,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_sla = tk.Entry(
            self.frm_dados,
            width = 20
        )
        self.txt_sla.grid(
            row = 2,
            column = 3,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.frm_botoes = tk.Frame(
            self.root,
            border = 2,
            relief = "groove"
        )
        self.frm_botoes.grid(
            row = 2,
            column = 0,
            padx = 10,
            pady = 5,
            columnspan = 4
        )
        self.btn_novo = tk.Button(
            self.frm_botoes,
            text = "Novo",
            width = 15
        )
        self.btn_novo.grid(
            row = 0,
            column = 0,
            padx = 5,
            pady = 5
        )
        self.btn_alterar = tk.Button(
            self.frm_botoes,
            text = "Alterar",
            width = 15
        )
        self.btn_alterar.grid(
            row = 0,
            column = 1,
            padx = 5,
            pady = 5
        )        
        self.btn_excluir = tk.Button(
            self.frm_botoes,
            text = "Excluir",
            width = 15
        )
        self.btn_excluir.grid(
            row = 0,
            column = 2,
            padx = 5,
            pady = 5
        )   
        self.btn_fechar = tk.Button(
            self.frm_botoes,
            text = "Fechar",
            width = 15
        )
        self.btn_fechar.grid(
            row = 0,
            column = 3,
            padx = 5,
            pady = 5
        )                 
    def configurar_treeview(self):
        pass
    def configurar_eventos(self):
        pass 

    def iniciar(self):
        self.root.mainloop()

f = Fornecedor_View(tk.Tk())
f.iniciar()