- Limpeza de dados de Sinistros
Esse repositório contem um script em Python desenvolvido para automatizar o tratamento e a limpeza de dados de uma planilha de sinistros. O script lê as regras de exclusão de colunas de um arquivo de configuração externo e realiza diversos tratamentos de dados.
Para o uso do script de forma rápida e fácil, basta acessar a ferramenta online Google Colab (disponível em https://colab.research.google.com/), **upar os arquivos necessários e rodá-lo :)**
- **Arquivos necessários:**
  - versao_xlsx.py: O código principal.
  - base de dados.txt: Arquivo de texto contendo a lista de colunas e o status (Sim/Não) para remoção.
  - 2025 SINISTROS.xlsx: A base de dados bruta original.
  *Nota: Para rodar arquivos de outros anos: basta alterar a data vigente referente ao arquivo de base no qual será upado.
         Para alterar os status de "Sim" e "Não".

- Funcionalidades
O script realiza as seguintes etapas de processamento:
  - Filtro Dinâmico de Colunas: Lê o arquivo base de dados.txt e identifica quais colunas devem ser removidas (baseado no status "Não").
  - Mesclagem de Dados: Soma as colunas de veículos "Outros" e "Não Disponível" em uma única coluna unificada.
  - Remoção de Duplicatas: Remove registros duplicados baseando-se no ID do sinistro.
  - Tratamento de Valores Nulos: Substitui valores vazios por 0 (exceto em coordenadas geográficas).
  - Padronização de Texto: Converte todos os campos de texto para CAIXA ALTA e remove espaços extras no início e fim.
  - Exportação Dupla: Gera o resultado final nos formatos .xlsx (Excel) e .csv.
