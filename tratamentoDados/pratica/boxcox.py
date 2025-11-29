# 002-exercicio-boxcox.py
# Seu desafio:
# 1. Crie uma série de dados assimétricos (você escolhe como gerar).
# 2. Aplique a transformação Box-Cox corretamente.
# 3. Salve o valor de lambda retornado.
# 4. Compare Box-Cox com log1p usando gráficos.
# 5. NÃO imprima nada além do lambda.

# Esqueleto para você completar:

import numpy as np
import pandas as pd
from scipy.stats import boxcox
import matplotlib.pyplot as plt

# 1. Gere seus dados assimétricos
rng = np.random.default_rng(42)
df_dados = pd.DataFrame(rng.integers(0, 100, size=((5, 10))))
#print(df_dados)

# 2. Aplique Box-Cox garantindo que todos os valores sejam > 0
df_dados_log1p = df_dados.select_dtypes(include=['int', 'float'])
df_dados_log1p = np.log1p(df_dados.select_dtypes(include=['int', 'float']))


df_dados_boxcox = pd.DataFrame()
for col in df_dados.columns:
    col_data = df_dados[col]
    col_data = col_data + 1 if col_data.min() <= 0 else col_data
    transformado, lambda_bc = boxcox(col_data)
    df_dados_boxcox[col] = transformado
print(df_dados_boxcox)

# 3. Imprima apenas o lambda
print(f'\nlambda_bc: {lambda_bc}')

# 4. Compare distribuições com 3 histogramas
#    (original, log1p, boxcox)
print(f'\nOriginal: \n{df_dados}')
print(f'\nlog1p: \n{df_dados_log1p}')
print(f'\nboxcox: \n{df_dados_boxcox}')