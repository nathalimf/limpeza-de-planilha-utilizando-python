# 🧹 Limpeza e Tratamento de Planilha de Sinistros (2025)

Este repositório contém um script em Python desenvolvido para automatizar o tratamento, a higienização e a padronização de dados de uma planilha de sinistros. O script utiliza regras dinâmicas de exclusão de colunas a partir de um arquivo de configuração externo, facilitando a manutenção do código.

---

## 🚀 Como Executar (Rápido e Fácil)

Para rodar o script sem precisar instalar nada no seu computador, você pode usar o **Google Colab**:

1. Acesse o [Google Colab](https://colab.research.google.com/).
2. Crie um novo notebook ou faça o upload do arquivo `versao_xlsx.py`.
3. Na barra lateral esquerda do Colab, clique no ícone de pasta (**Arquivos**) e faça o upload dos arquivos necessários listados abaixo.
4. Execute o código! :)

### 📁 Arquivos Necessários

| Arquivo | Descrição |
| :--- | :--- |
| `versao_xlsx.py` | O código principal do script. |
| `base de dados.txt` | Arquivo de texto com a lista de colunas e o status (`Sim`/`Não`) para remoção. |
| `2025 SINISTROS.xlsx` | A base de dados bruta original de sinistros. |

> 💡 **Nota de Customização:** > - **Outros Anos:** Caso queira processar dados de outros anos, basta alterar o nome do arquivo de entrada no código para a data correspondente e fazer o upload dele.
> - **Alterar Colunas Excluídas:** Basta abrir o arquivo `base de dados.txt` e alterar o status para `Não` na coluna que deseja remover.

---

## 🛠️ Funcionalidades do Script

O script realiza as seguintes etapas automatizadas de processamento:

* **Filtro Dinâmico de Colunas:** Lê o arquivo `base de dados.txt` e remove automaticamente as colunas marcadas com o status `"Não"`.
* **Mesclagem de Dados (Regra de Negócio):** Soma as colunas de veículos `qtd_veic_outros` e `qtd_veic_nao_disponivel` em uma única coluna unificada.
* **Remoção de Duplicatas:** Identifica e remove registros duplicados baseando-se no ID único do sinistro (`id_sinistro`), mantendo apenas a primeira ocorrência.
* **Tratamento de Valores Nulos:** Substitui valores vazios por `0` em colunas numéricas gerais. As colunas de coordenadas geográficas (`latitude`/`longitude`) são preservadas como nulas para não distorcer mapas.
* **Padronização de Texto:** Converte todos os campos textuais para **CAIXA ALTA** e remove espaços em branco extras no início e no fim das frases.
* **Exportação Dupla:** Gera simultaneamente dois arquivos finais tratados:
  - `.xlsx`: Pronto para conferência visual no Excel.
  - `.csv`: Formatado e otimizado para importação direta em bancos de dados.

---

## 🧰 Tecnologias Utilizadas

- **Python 3**
- **Pandas** (Manipulação de dados)
- **OpenPyXL** (Suporte para leitura/escrita de arquivos Excel)
