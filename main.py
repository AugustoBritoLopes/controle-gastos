import gspread
from datetime import datetime
import sys
import os


DIRETORIO_DO_SCRIPT = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_CREDENCIAIS = os.path.join(DIRETORIO_DO_SCRIPT, "credentials.json")
NOME_PLANILHA = "Controle-Gastos" 

def conectar():
    try:
        gc = gspread.service_account(filename=ARQUIVO_CREDENCIAIS)
        return gc.open(NOME_PLANILHA).sheet1
    except Exception as e:
        print(f"❌ Erro de conexão: {e}")
        print(f"Tentando ler credenciais em: {ARQUIVO_CREDENCIAIS}")
        sys.exit(1)

def encontrar_posicao(lista, item):
    item_limpo = str(item).lower().strip()
    for i, valor in enumerate(lista):
        if str(valor).lower().strip() == item_limpo:
            return i + 1 
    return None

def adicionar_gasto(categoria, valor):
    ws = conectar()
    mes_atual = datetime.now().strftime("%b_%Y").lower()
    
    cabecalho = ws.row_values(1)
    col_index = encontrar_posicao(cabecalho, mes_atual)
    
    if not col_index:
        col_index = len(cabecalho) + 1
        ws.update_cell(1, col_index, mes_atual)

    categorias = ws.col_values(1)
    row_index = encontrar_posicao(categorias, categoria)
    
    if not row_index:
        row_index = len(categorias) + 1
        ws.update_cell(row_index, 1, categoria.title())

    valor_celula = ws.cell(row_index, col_index).value
    try:
        valor_anterior = float(valor_celula.replace(',', '.')) if valor_celula else 0.0
    except ValueError:
        valor_anterior = 0.0
        
    novo_total = valor_anterior + valor
    ws.update_cell(row_index, col_index, novo_total)
    
    print(f"✅ R$ {valor:.2f} adicionado em '{categoria.upper()}' (Total Mês: R$ {novo_total:.2f})")

def processar_entrada(args):
    try:
        valor_str = args[-1].replace(',', '.')
        valor = float(valor_str)
        
        categoria = " ".join(args[:-1]) 
        
        if not categoria:
            print("❌ Erro: Faltou a categoria.")
            return

        adicionar_gasto(categoria, valor)
    except ValueError:
        print("❌ Erro: O último item deve ser um valor numérico.")
        print("   Ex: gasto mercado 50.00")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        processar_entrada(sys.argv[1:])
    else:
        print("--- Modo Interativo ---")
        while True:
            entrada = input("Digite <categoria> <valor> (ou sair): ").strip()
            if entrada.lower() in ['sair', 'exit']: break
            if entrada: processar_entrada(entrada.split())