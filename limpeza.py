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

nome_arquivo_excel = '2025 SINISTROS.xlsx'

if os.path.exists(nome_arquivo_excel):
    df = pd.read_excel(nome_arquivo_excel)

    df = df.drop(columns=colunas_para_remover, errors='ignore')

    # mesclagem de colunas conforme código de Juliana
    cols_para_somar = ['qtd_veic_outros', 'qtd_veic_nao_disponivel']
    if all(col in df.columns for col in cols_para_somar):
        df['qtd_veic_outros_não_dispo'] = df['qtd_veic_outros'].fillna(0) + df['qtd_veic_nao_disponivel'].fillna(0)
        df = df.drop(columns=cols_para_somar)
        print("Colunas mescladas com sucesso.")

    if 'id_sinistro' in df.columns:
        antes = len(df)
        df = df.drop_duplicates(subset=['id_sinistro'], keep='first')
        print(f"Duplicatas removidas: {antes - len(df)} linhas.")
    else:
        df = df.drop_duplicates()

    df = df.fillna(0)

    colunas_geo = ['latitude', 'longitude']
    for col in colunas_geo:
        if col in df.columns:
            df.loc[df[col] == 0, col] = None

    colunas_texto = df.select_dtypes(include=['object']).columns
    for col in colunas_texto:
        df[col] = df[col].apply(lambda x: str(x).upper().strip() if x is not None else x)

    # exportação
    nome_saida_xlsx = '2025 SINISTROS LIMPA.xlsx'
    nome_saida_csv = '2025 SINISTROS LIMPA.csv'
    
    df.to_excel(nome_saida_xlsx, index=False)
    
    df.to_csv(nome_saida_csv, index=False, sep=';', encoding='utf-8-sig')
    
    print(f"Sucesso! Arquivos gerados:\n- {nome_saida_xlsx}\n- {nome_saida_csv}")
else:
    print(f"Erro: O arquivo {nome_arquivo_excel} não foi encontrado.")
