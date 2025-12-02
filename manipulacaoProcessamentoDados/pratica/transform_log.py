# Exercício 002 - Transformação Logarítmica com np.log1p
# ======================================================
# Tarefa: completar o código abaixo.
# Objetivo: aplicar np.log1p em uma coluna de um DataFrame.

import numpy as np
import pandas as pd

# Dataset de exemplo: pontuação de ninjas (Naruto!) em missões
# complete os valores você mesmo
pontos = pd.DataFrame({
    "ninja": ["Naruto", "Sasuke", "Sakura", "Kakashi"],
    "pontuacao": [10 , 50 , 0 , 120 ]  # complete aqui com valores inteiros
})

# TODO 1: aplicar transformação log1p na coluna "pontuacao"
# e salvar em uma nova coluna chamada "pontuacao_log"
pontos["pontuacao_log"] = np.log1p(pontos['pontuacao'])

print(pontos)

# Quando terminar, responda: "Feito" ou "Preciso de uma dica"
