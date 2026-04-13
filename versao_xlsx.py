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

nome_arquivo_csv = '2025 SINISTROS.csv' 

if os.path.exists(nome_arquivo_csv):
    df = pd.read_csv(nome_arquivo_csv, sep=';', encoding='latin-1')

    df = df.drop(columns=colunas_para_remover, errors='ignore')

    if 'id_sinistro' in df.columns:
        antes = len(df)
        df = df.drop_duplicates(subset=['id_sinistro'], keep='first')
        print(f"Duplicatas removidas: {antes - len(df)} linhas.")
    else:
        df = df.drop_duplicates()
        print("Aviso: 'id_sinistro' não encontrado.")

    df = df.fillna(0)

    colunas_texto = df.select_dtypes(include=['object']).columns
    for col in colunas_texto:
        df[col] = df[col].apply(lambda x: str(x).upper().strip() if not isinstance(x, (int, float)) else x)

    nome_saida = '2025 SINISTROS LIMPA.csv'
    df.to_csv(nome_saida, index=False, sep=';', encoding='utf-8-sig')
    print(f"Sucesso! Arquivo '{nome_saida}' pronto.")
else:
    print(f"Erro: O arquivo {nome_arquivo_csv} não foi encontrado.")
