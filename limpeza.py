# 100% ARRUMADO, usar ESSE A2QUIIIIIIIIIIII

import pandas as pd
import os

colunas_para_remover = []

try:
    with open('base de dados.txt', 'r', encoding='utf-8') as file:
        for linha in file:
            if ':' in linha:
                partes = linha.split(':', 1)
                nome_coluna = partes[0].strip()
                if "source" in nome_coluna.lower():
                    continue
                status = partes[1].strip()
                if status == "Não":
                    colunas_para_remover.append(nome_coluna)
except FileNotFoundError:
    print("Aviso: Arquivo 'base de dados.txt' não encontrado.")

nome_arquivo_excel = '2023 SINISTROS.xlsx'

# 2. Processamento dos dados
if os.path.exists(nome_arquivo_excel):
    # Lemos o arquivo original
    df = pd.read_excel(nome_arquivo_excel)

    # Remove colunas indesejadas (conforme o seu .txt)
    df = df.drop(columns=colunas_para_remover, errors='ignore')

    # Mesclagem de colunas de veículos (Regra da Juliana)
    cols_para_somar = ['qtd_veic_outros', 'qtd_veic_nao_disponivel']
    if all(col in df.columns for col in cols_para_somar):
        df['qtd_veic_outros_não_dispo'] = df['qtd_veic_outros'].fillna(0) + df['qtd_veic_nao_disponivel'].fillna(0)
        df = df.drop(columns=cols_para_somar)
        print("Colunas de veículos mescladas.")

    # Tratamento de duplicatas por ID
    if 'id_sinistro' in df.columns:
        antes = len(df)
        df = df.drop_duplicates(subset=['id_sinistro'], keep='first')
        print(f"Duplicatas removidas: {antes - len(df)} linhas.")
    else:
        df = df.drop_duplicates()

    # --- AJUSTE DE PRECISÃO E VALORES NULOS ---
    # Definimos as colunas que NÃO devem ser preenchidas com 0 genericamente (Geo)
    colunas_geo = ['latitude', 'longitude']

    # Preenchemos com 0 apenas as colunas que não são de coordenadas
    cols_para_preencher_zero = [c for c in df.columns if c not in colunas_geo]
    df[cols_para_preencher_zero] = df[cols_para_preencher_zero].fillna(0)

    # Garante que latitude e longitude sejam tratadas como números decimais de alta precisão
    for col in colunas_geo:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            # Transformamos o 0 em nulo (None) para o banco de dados não achar que é no meio do oceano
            df.loc[df[col] == 0, col] = None

    # Padronização de texto (MAIÚSCULAS e limpeza de espaços)
    colunas_texto = df.select_dtypes(include=['object']).columns
    for col in colunas_texto:
        df[col] = df[col].apply(lambda x: str(x).upper().strip() if pd.notnull(x) and x != 0 else x)

    # 3. Exportação dos arquivos
    nome_saida_xlsx = '2023 SINISTROS LIMPA.xlsx'
    nome_saida_csv = '2023 SINISTROS LIMPA.csv'

    # Salva Excel para conferência visual
    df.to_excel(nome_saida_xlsx, index=False)

    # Salva CSV com separador de VÍRGULA e sem o caractere extra do Excel (BOM)
    # O encoding 'utf-8' puro resolve o problema dos ";" extras no final
    df.to_csv(nome_saida_csv, index=False, sep=',', encoding='utf-8', quoting=0)

    print(f"\nSucesso total! Arquivos gerados:")
    print(f"- Excel: {nome_saida_xlsx}")
    print(f"- CSV (Pronto para o Banco): {nome_saida_csv}")
else:
   print(f"Erro: O arquivo {nome_arquivo_excel} não foi encontrado.")
