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

# Calculando o risco do projeto com base nos três parâmetros (fictício: média)
risco = ((experiencia + investimento + prazo)/3).astype(int)

# Criando o DataFrame
df = pd.DataFrame({
    "Equipe": equipes,
    "Experiência (0-100)": experiencia,
    "Investimento (0-100)": investimento,
    "Prazo (0-100)": prazo,
    "Risco do Projeto": risco
})

# Salvando a planilha em formato Excel
file_path = "equipes_projeto.xlsx"
df.to_excel(file_path, index=False)

file_path