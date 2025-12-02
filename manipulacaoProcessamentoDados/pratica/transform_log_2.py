# Exercício 003 - Transformação Logarítmica Avançada
# ==================================================
# Objetivo: praticar transformação logarítmica em múltiplas colunas
# e detectar automaticamente quais precisam da transformação.

import numpy as np
import pandas as pd

# Dataset: estatísticas de jogadores de basquete
# Valores grandes e pequenos misturados

dados = pd.DataFrame({
    "jogador": ["Naruto", "Sasuke", "Sakura", "Kakashi"],
    "pontos": [1, 50, 300, 1200],
    "rebotes": [0, 1, 4, 20],
    "arremessos_errados": [2, 10, 80, 300]
})

# Tarefa:
# 1. Identificar automaticamente todas as colunas numéricas do DataFrame (exceto "jogador").
print(dados.select_dtypes(include=['int', 'float']))
# 2. Criar uma nova versão do dataframe chamada `dados_log`.
dados_log = dados.select_dtypes(include=['int', 'float'])
# 3. Para todas as colunas numéricas, aplicar np.log1p.
dados_log = np.log1p(dados.select_dtypes(include=['int', 'float']))
# 4. Imprimir o dataframe original e o transformado.
print("\nOriginal:")
print(dados)
print("\nTransformado:")
print(dados_log)  # esta variável deve ser criada por você

# Dicas permitidas (não use até precisar):
# - selecione colunas numéricas com: dados.select_dtypes(include=["int", "float"])
# - copie o DataFrame usando: dados.copy()
# - aplique log com: np.log1p(...)