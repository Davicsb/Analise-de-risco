import pandas as pd
import numpy as np

# Dados para a criação da planilha
num_equipes = 100  # Número de equipes fictícias
np.random.seed(42)  # Semente para reprodução dos resultados

# Gerando dados aleatórios
equipes = [f"Equipe {i+1}" for i in range(num_equipes)]
experiencia = np.random.randint(0, 101, num_equipes)
investimento = np.random.randint(0, 101, num_equipes)
prazo = np.random.randint(0, 101, num_equipes)
complexidade = np.random.randint(0, 101, num_equipes)
demanda = np.random.randint(0, 101, num_equipes)
dependencia = np.random.randint(0, 101, num_equipes)

# Criando o DataFrame
df = pd.DataFrame({
    "Equipe": equipes,
    "Experiência (0-100)": experiencia,
    "Investimento (0-100)": investimento,
    "Prazo (0-100)": prazo,
    "Complexidade do projeto (0-100)": complexidade, 
    "Demanda do mercado (0-100)": demanda,
    "Dependência da tecnologia de terceiros (0-100)": dependencia 
})

# Salvando a planilha em formato Excel
file_path = "equipes_projeto.xlsx"
df.to_excel(file_path, index=False)

file_path
