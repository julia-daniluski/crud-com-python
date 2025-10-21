import tkinter as tk
from tkinter import ttk
from db import ensuredb
from utils import centralizarjanela
from login import showlogin
from comidas import showcomidas
from estoque import showgestaoestoque

class App(tk.Tk):
    """
    Classe principal do aplicativo.
    Herda de tk.Tk, ou seja, é a janela principal do Tkinter.
    """
    def __init__(self):
        super().__init__()
        self.title("Controle de Estoque: Comidas Nordestinas")

        # Inicializa o banco de dados
        ensuredb()

        # Usuário logado
        self.currentuser = None

        # Centraliza a janela de login
        centralizarjanela(self, 400, 250)

        # Exibe a tela de login
        showlogin(self)

    def showmain(self):
        """
        Mostra o menu principal após login bem-sucedido.
        """
        # Limpa a tela antiga (login)
        for w in self.winfo_children():
            w.destroy()

        # Centraliza e expande a janela para modo principal
        centralizarjanela(self, 1000, 550)

        # Frame superior com dados do usuário e botões de navegação
        top = ttk.Frame(self, padding=2)
        top.pack(fill="x")

        # Exibe quem está logado
        ttk.Label(top, text=f"Usuário logado: {self.currentuser.get('nome_completo','')}").pack(side="left")

        # Botão Sair
        ttk.Button(top, text="Sair", command=lambda: showlogin(self)).pack(side="right")

        # Botão Cadastro de Comidas
        ttk.Button(top, text="Cadastro de Comidas", command=lambda: showcomidas(self)).pack(side="right", padx=6)

        # Botão Gestão de Estoque
        ttk.Button(top, text="Gestão de Estoque", command=lambda: showgestaoestoque(self)).pack(side="right", padx=6)

        # Frame central com mensagem de boas-vindas
        center = ttk.Frame(self, padding=40)
        center.pack(expand=True)

        msg = (
            f"Olá, {self.currentuser.get('nome_completo','')}!\n"
            "Bem-vindo ao sistema de controle de estoque de Comidas Nordestinas.\n\n"
            "Aqui você pode:\n"
            " ** Cadastrar novos pratos e comidas típicas\n"
            " ** Consultar e editar o estoque\n"
            " ** Registrar entradas e saídas\n\n"
            "Escolha um botão na barra de opções acima para começar."
        )

        tk.Label(center, text=msg, font=("TkDefaultFont", 18), justify="left").pack()


# --- Ponto de entrada do programa ---
if __name__ == "__main__":
    app = App()
    app.mainloop()
