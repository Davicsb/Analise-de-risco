# import pandas lib as pd
import pandas as pd
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# ler a sheet
caminho = input("digite o caminho do arquivo, ex: \'C:\\Users\\nome\\OneDrive\\Documentos\\equipes projeto.xlsx\' ")
df = pd.read_excel(caminho)

# Obtendo o número de linhas e colunas
num_linhas, num_colunas = df.shape

print(f'Número de linhas: {num_linhas}') #101
print(f'Número de colunas: {num_colunas}') #4 nome, exp, invest e prazo

#Criando as funções de pertinencia, como vai de 0 a 100 deixei elas bem simples

experiencia = ctrl.Antecedent(np.arange(0, 101, 10), 'experiência')
investimento = ctrl.Antecedent(np.arange(0, 101, 10), 'investimento')
prazo = ctrl.Antecedent(np.arange(0, 101, 10), 'prazo')

experiencia['Baixa'] = fuzz.trapmf(experiencia.universe, [0, 0, 20, 50])
experiencia['Media'] = fuzz.trimf(experiencia.universe, [30, 50, 70])
experiencia['Alta'] = fuzz.trapmf(experiencia.universe, [50, 80, 100, 100])

investimento['Baixo'] = fuzz.trapmf(experiencia.universe, [0, 0, 20, 50])
investimento['Medio'] = fuzz.trimf(experiencia.universe, [30, 50, 70])
investimento['Alto'] = fuzz.trapmf(experiencia.universe, [50, 80, 100, 100])

prazo['Curto'] = fuzz.trapmf(experiencia.universe, [0, 0, 20, 50])
prazo['Medio'] = fuzz.trimf(experiencia.universe, [30, 50, 70])
prazo['Longo'] = fuzz.trapmf(experiencia.universe, [50, 80, 100, 100])

#se quiser ver o grafico delas só descomentar
#experiencia.view()

#-- regras -- 

#-- risco baixo --

# exp MÉDIA e invest ALTO e prazo LONGO = risco baixo 
regra1 = ctrl.Rule(experiencia['Baixa'], investimento['Alto'], prazo['Longo'])
# exp ALTA e invest BAIXO e prazo LONGO = risco baixo
regra2 = ctrl.Rule(experiencia['Alta'], investimento['Baixo'], prazo['Longo'])
# exp ALTA e invest ALTO e prazo CURTO = risco baixo
regra3 = ctrl.Rule(experiencia['Alta'], investimento['Alto'], prazo['Curto'])

#----------------

#-- risco médio --

# exp BAIXA e invest BAIXO e prazo CURTO = risco médio
regra4 = ctrl.Rule(experiencia['Baixa'], investimento['Baixo'], prazo['Curto'])
# exp MÉDIA e invest MÉDIO e prazo MÉDIO = risco médio
regra5 = ctrl.Rule(experiencia['Media'], investimento['Medio'], prazo['Medio'])
# exp ALTA e invest MÉDIO e prazo CURTO = risco médio
regra6 = ctrl.Rule(experiencia['Alta'], investimento['Medio'], prazo['Curto'])

#----------------

#-- risco alto --

# exp BAIXA e invest ALTO e prazo CURTO = risco alto
regra7 = ctrl.Rule(experiencia['Baixa'], investimento['Alto'], prazo['Curto'])
# exp BAIXA e invest BAIXO e prazo LONGO = risco alto
regra8 = ctrl.Rule(experiencia['Baixa'], investimento['Baixo'], prazo['Longo'])

#---------------

#----------

#use df.iat[x,y] pra pegar as informações da tabela ([i, 0] == nome ... [i, 3] == prazo)
