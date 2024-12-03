import pandas as pd
import numpy as np

# Dados para a criação da planilha
num_equipes = 100  # Número de equipes fictícias

# Gerando dados aleatórios
equipes = [f"Equipe {i+1}" for i in range(num_equipes)]
experiencia = np.random.randint(0, 101, num_equipes)
investimento = np.random.randint(0, 101, num_equipes)
prazo = np.random.randint(0, 101, num_equipes)
complexidade = np.random.randint(0, 101, num_equipes)
demanda = np.random.randint(0, 101, num_equipes)
dependencia = np.random.randint(0, 101, num_equipes)
tamanho = np.random.randint(0, 101, num_equipes)
historico = np.random.randint(0, 101, num_equipes)
carga = np.random.randint(0, 101, num_equipes)
escopo = np.random.randint(0, 101, num_equipes)

# Criando o DataFrame
df = pd.DataFrame({
    "Equipe": equipes,
    "Experiência (0-100)": experiencia,
    "Investimento (0-100)": investimento,
    "Prazo (0-100)": prazo,
    "Complexidade do projeto (0-100)": complexidade, 
    "Demanda do mercado (0-100)": demanda,
    "Dependência da tecnologia de terceiros (0-100)": dependencia,
    "Tamanho da equipe (0-100)" : tamanho,
    "Histórico de sucesso da equipe": historico,
    "Carga horária da equipe (0-100)": carga,
    "Escopo do projeto (0-100)": escopo
})

# Salvando a planilha em formato Excel
file_path = "equipes_projeto.xlsx"
df.to_excel(file_path, index=False)
print("Dados cadastrados com sucesso!")
file_path
