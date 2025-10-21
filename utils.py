# Importa o módulo do tkinter para recursos extras de interface.
import tkinter as tk  

# Importa o método para abrir conexões com o banco de dados.
from db import getconnection  

def mergesortproducts(products, key="nome"):
    """
    Ordena lista de comidas por atributo escolhido.
    Utiliza o algoritmo mergesort para garantir ordenação estável, eficiente e insensível a maiúsculas/minúsculas.
    """
    if len(products) <= 1:
        return products

    mid = len(products) // 2
    left = mergesortproducts(products[:mid], key)
    right = mergesortproducts(products[mid:], key)

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if str(left[i][key]).lower() < str(right[j][key]).lower():
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def centralizarjanela(win, largura=800, altura=600):
    """Centraliza uma janela Tkinter na tela."""
    win.update_idletasks()
    screenw = win.winfo_screenwidth()
    screenh = win.winfo_screenheight()
    x = screenw // 2 - largura // 2
    y = screenh // 2 - altura // 2
    win.geometry(f"{largura}x{altura}+{x}+{y}")

# --- Função para Gerar Código de Produto ---
# Cria um código único para cada nova comida (ex: C001, C002)
def gerarcodigo():
    with getconnection() as conn:
        # Busca o id mais alto da tabela de comidas
        cur = conn.execute("SELECT id FROM comidas ORDER BY id DESC LIMIT 1")
        row = cur.fetchone()
        # Se não houver cadastros, retorna o primeiro código padrão
        if not row:
            return "C001"
        # Gera o próximo código baseado no maior id atual, preenchendo com zeros à esquerda
        return f"C{row['id'] + 1:03d}"
