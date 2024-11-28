# import pandas lib as pd
import pandas as pd
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# variaveis:
# experiencia da equipe, investimento, prazo, complexidade do projeto, demanda do mercado, dependencia da tecnologia de terceiros, tamanho da equipe, histórico de sucesso, carga de trabalho e escopo


# ler a sheet
caminho = input("digite o caminho do arquivo, ex: \'C:\\Users\\nome\\OneDrive\\Documentos\\equipes projeto.xlsx\' ")
df = pd.read_excel(caminho)

# Obtendo o número de linhas e colunas
num_linhas, num_colunas = df.shape

#Criando as funções de pertinencia, como vai de 0 a 100 deixei elas bem simples

risco = ctrl.Consequent(np.arange(0, 101, 10), 'risco')

experiencia = ctrl.Antecedent(np.arange(0, 101, 10), 'experiência')
investimento = ctrl.Antecedent(np.arange(0, 101, 10), 'investimento')
prazo = ctrl.Antecedent(np.arange(0, 101, 10), 'prazo')

complexidade_do_projeto = ctrl.Antecedent(np.arange(0, 101, 10), 'complexidade do projeto')
demanda_do_mercado = ctrl.Antecedent(np.arange(0, 101, 10), 'demanda do mercado')
dependencia_de_terceiros = ctrl.Antecedent(np.arange(0, 101, 10), 'dependencia de terceiros')

tamanho_da_equipe = ctrl.Antecedent(np.arange(0, 101, 10), 'tamanho da equipe')
historico_de_sucesso = ctrl.Antecedent(np.arange(0, 101, 10), 'historico de sucesso')
carga_de_trabalho = ctrl.Antecedent(np.arange(0, 101, 10), 'carga de trabalho')
escopo_do_projeto = ctrl.Antecedent(np.arange(0, 101, 10), 'escopo do projeto')

#------
risco['Baixo'] = fuzz.trapmf(risco.universe, [0, 0, 20, 50])
risco['Medio'] = fuzz.trimf(risco.universe, [30, 50, 70])
risco['Alto'] = fuzz.trapmf(risco.universe, [50, 80, 100, 100])

experiencia['Baixa'] = fuzz.trapmf(experiencia.universe, [0, 0, 20, 50])
experiencia['Media'] = fuzz.trimf(experiencia.universe, [30, 50, 70])
experiencia['Alta'] = fuzz.trapmf(experiencia.universe, [50, 80, 100, 100])
#
investimento['Baixo'] = fuzz.trapmf(investimento.universe, [0, 0, 20, 50])
investimento['Medio'] = fuzz.trimf(investimento.universe, [30, 50, 70])
investimento['Alto'] = fuzz.trapmf(investimento.universe, [50, 80, 100, 100])
#
prazo['Curto'] = fuzz.trapmf(prazo.universe, [0, 0, 20, 50])
prazo['Medio'] = fuzz.trimf(prazo.universe, [30, 50, 70])
prazo['Longo'] = fuzz.trapmf(prazo.universe, [50, 80, 100, 100])


complexidade_do_projeto['Baixa'] = fuzz.trapmf(complexidade_do_projeto.universe, [0, 0, 20, 50])
complexidade_do_projeto['Media'] = fuzz.trimf(complexidade_do_projeto.universe, [30, 50, 70])
complexidade_do_projeto['Alta'] = fuzz.trapmf(complexidade_do_projeto.universe, [50, 80, 100, 100])
#
demanda_do_mercado['Baixa'] = fuzz.trapmf(demanda_do_mercado.universe, [0, 0, 20, 50])
demanda_do_mercado['Media'] = fuzz.trimf(demanda_do_mercado.universe, [30, 50, 70])
demanda_do_mercado['Alta'] = fuzz.trapmf(demanda_do_mercado.universe, [50, 80, 100, 100])
#
dependencia_de_terceiros['Baixa'] = fuzz.trapmf(dependencia_de_terceiros.universe, [0, 0, 20, 50])
dependencia_de_terceiros['Media'] = fuzz.trimf(dependencia_de_terceiros.universe, [30, 50, 70])
dependencia_de_terceiros['Alta'] = fuzz.trapmf(dependencia_de_terceiros.universe, [50, 80, 100, 100])


tamanho_da_equipe['Pequeno'] = fuzz.trapmf(tamanho_da_equipe.universe, [0, 0, 20, 50])
tamanho_da_equipe['Medio'] = fuzz.trimf(tamanho_da_equipe.universe, [30, 50, 70])
tamanho_da_equipe['Grande'] = fuzz.trapmf(tamanho_da_equipe.universe, [50, 80, 100, 100])
#
historico_de_sucesso['Baixo'] = fuzz.trapmf(historico_de_sucesso.universe, [0, 0, 20, 50])
historico_de_sucesso['Medio'] = fuzz.trimf(historico_de_sucesso.universe, [30, 50, 70])
historico_de_sucesso['Alto'] = fuzz.trapmf(historico_de_sucesso.universe, [50, 80, 100, 100])
#
carga_de_trabalho['Baixa'] = fuzz.trapmf(carga_de_trabalho.universe, [0, 0, 20, 50])
carga_de_trabalho['Media'] = fuzz.trimf(carga_de_trabalho.universe, [30, 50, 70])
carga_de_trabalho['Alta'] = fuzz.trapmf(carga_de_trabalho.universe, [50, 80, 100, 100])
#
escopo_do_projeto['Pequeno'] = fuzz.trapmf(escopo_do_projeto.universe, [0, 0, 20, 50])
escopo_do_projeto['Medio'] = fuzz.trimf(escopo_do_projeto.universe, [30, 50, 70])
escopo_do_projeto['Grande'] = fuzz.trapmf(escopo_do_projeto.universe, [50, 80, 100, 100])

#se quiser ver o grafico delas só descomentar
#experiencia.view()

#-- regras -- 

#-- risco baixo --

#experiência alta e a demanda alta e o histórico de sucesso é alto, então o risco é baixo.
regra1 = ctrl.Rule(experiencia['Alta'] & demanda_do_mercado['Alta'] & historico_de_sucesso['Alto'], risco['Baixo'])
#investimento alto e o prazo longo e a experiência da equipe alta, então o risco é baixo.
regra2 = ctrl.Rule(investimento['Alto'] & prazo['Longo'] & experiencia['Alta'], risco['Baixo'])
#experiência da equipe alta e a complexidade do projeto baixa e a carga de trabalho baixa, então o risco é baixo.
regra3 = ctrl.Rule(experiencia['Alta'] & complexidade_do_projeto['Baixa'] & carga_de_trabalho['Baixa'], risco['Baixo'])
#demanda do mercado alta e o escopo pequeno e a experiência da equipe alta, então o risco é baixo.
regra4 = ctrl.Rule(demanda_do_mercado['Alta'] & escopo_do_projeto['Pequeno'] & experiencia['Alta'], risco['Baixo'])
#prazo médio e a carga de trabalho média e a dependência de tecnologia de terceiros baixa, então o risco é baixo.
regra5 = ctrl.Rule(prazo['Medio'] & carga_de_trabalho['Media'] & dependencia_de_terceiros['Baixa'], risco['Baixo'])
#experiência da equipe alta e o investimento médio e a dependência de tecnologia de terceiros baixa, então o risco é baixo.
regra6 = ctrl.Rule(experiencia['Alta'] & investimento['Medio'] & dependencia_de_terceiros['Baixa'], risco['Baixo'])
#investimento é alto e o prazo longo e o histórico de sucesso alto, então o risco é baixo.
regra7 = ctrl.Rule(investimento['Alto'] & prazo['Longo'] & historico_de_sucesso['Alto'], risco['Baixo'])

#----------------

#-- risco médio --

#demanda do mercado média e a dependência de tecnologia de terceiros média e o escopo médio, então o risco é médio.
regra8 = ctrl.Rule(demanda_do_mercado['Media'] & dependencia_de_terceiros['Media'] & escopo_do_projeto['Medio'], risco['Medio'])
#experiência da equipe média e o investimento médio e o tamanho da equipe média, então o risco é médio.
regra9 = ctrl.Rule(experiencia['Media'] & investimento['Medio'] & tamanho_da_equipe['Medio'], risco['Medio'])
#tamanho da equipe grande e a carga de trabalho alta e a complexidade do projeto média, então o risco é médio.
regra10 = ctrl.Rule(tamanho_da_equipe['Grande'] & carga_de_trabalho['Alta'] & complexidade_do_projeto['Media'], risco['Medio'])

#----------------

#-- risco alto --
#experiência da equipe baixa e a complexidade do projeto alta e a dependência de tecnologia de terceiros alta, então o risco é alto.
regra11 = ctrl.Rule(experiencia['Baixa'] & complexidade_do_projeto['Alta'] & dependencia_de_terceiros['Alta'], risco['Alto'])
#investimento baixo e o prazo curto e o escopo grande, então o risco é alto.
regra12 = ctrl.Rule(investimento['Baixo'] & prazo['Curto'] & escopo_do_projeto['Grande'], risco['Alto'])
#experiência da equipe média e o tamanho da equipe pequena e a carga de trabalho alta, então o risco é alto.
regra13 = ctrl.Rule(experiencia['Media'] & tamanho_da_equipe['Pequeno'] & carga_de_trabalho['Alta'], risco['Alto'])
#experiência da equipe baixa e o investimento baixo e a complexidade do projeto alta, então o risco é alto.
regra14 = ctrl.Rule(experiencia['Baixa'] & investimento['Baixo'] & complexidade_do_projeto['Alta'], risco['Alto'])
#prazo curto e o tamanho da equipe pequena e o escopo grande, então o risco é alto.
regra15 = ctrl.Rule(prazo['Curto'] & tamanho_da_equipe['Pequeno'] & escopo_do_projeto['Grande'], risco['Alto'])
#carga de trabalho alta e a experiência da equipe baixa e o histórico de sucesso baixo, então o risco é alto.
regra16 = ctrl.Rule(carga_de_trabalho['Alta'] & experiencia['Baixa'] & historico_de_sucesso['Baixo'], risco['Alto'])
#investimento baixo e o histórico de sucesso baixo e o prazo curto, então o risco é alto.
regra17 = ctrl.Rule(investimento['Baixo'] & historico_de_sucesso['Baixo'] & prazo['Curto'], risco['Alto'])
#complexidade do projeto alta e a experiência da equipe baixa e o escopo grande, então o risco é alto.
regra18 = ctrl.Rule(complexidade_do_projeto['Alta'] & experiencia['Baixa'] & escopo_do_projeto['Grande'], risco['Alto'])
#prazo curto e a demanda do mercado alta e o histórico de sucesso baixo, então o risco é alto.
regra19 = ctrl.Rule(prazo['Curto'] & demanda_do_mercado['Alta'] & historico_de_sucesso['Baixo'], risco['Alto'])
#Se o escopo é grande e a experiência da equipe é média e a dependência de tecnologia de terceiros é alta, então o risco é alto.
regra20 = ctrl.Rule(escopo_do_projeto['Grande'] & experiencia['Media'] & dependencia_de_terceiros['Alta'], risco['Alto'])

#---------------

risco_ctrl = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9, regra10, regra11, regra12, regra13, regra14, regra15, regra16, regra17, regra18, regra19, regra20])
risco_simul = ctrl.ControlSystemSimulation(risco_ctrl)

#----------

# Criar uma coluna para o risco calculado
df['Risco'] = np.nan

# Calcular o risco para cada linha e salvar na última coluna
for i in range(len(df)):
    try:
        risco_simul.input['experiência'] = df.iloc[i, 1]
        risco_simul.input['investimento'] = df.iloc[i, 2]
        risco_simul.input['prazo'] = df.iloc[i, 3]
        risco_simul.input['complexidade do projeto'] = df.iloc[i, 4]
        risco_simul.input['demanda do mercado'] = df.iloc[i, 5]
        risco_simul.input['dependencia de terceiros'] = df.iloc[i, 6]
        risco_simul.input['tamanho da equipe'] = df.iloc[i, 7]
        risco_simul.input['historico de sucesso'] = df.iloc[i, 8]
        risco_simul.input['carga de trabalho'] = df.iloc[i, 9]
        risco_simul.input['escopo do projeto'] = df.iloc[i, 10]

        risco_simul.compute()
        df.at[i, 'Risco'] = risco_simul.output['risco']
    except Exception as e:
        print(f"Erro na linha {i}: {e}")
        df.at[i, 'Risco'] = None

# Salvar o resultado em uma nova planilha
caminho_saida = caminho.replace('.xlsx', '_com_risco.xlsx')
df.to_excel(caminho_saida, index=False)
print(f"Arquivo salvo com os riscos calculados em: {caminho_saida}")