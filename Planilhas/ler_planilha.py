import pandas as pd

# Carrega a planilha sem considerar a primeira linha como cabeçalho
df = pd.read_excel('equipes_projeto.xlsx')

# Salva os dados em um arquivo de texto
with open('dados.txt', 'w') as f:
    # Escreve o conteúdo da tabela linha por linha no arquivo .txt
    for index, row in df.iterrows():
        # Converte cada linha para string e escreve no arquivo
        f.write('\t'.join(map(str, row.values)) + '\n')
print("Dados cadastrados com sucesso!")