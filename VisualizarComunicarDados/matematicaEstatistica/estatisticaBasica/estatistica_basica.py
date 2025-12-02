import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('D:/GitHub/Cursos-EBAC/VisualizarComunicarDados/matematicaEstatistica/estatisticaBasica/clientes-v3-preparado.csv')

print(df.head(15))

print('Estatística com Pandas')
print(f"Média: {df['salario'].mean()}")
print(f"Mediana: {df['salario'].median()}")
print(f"Variancia: {df['salario'].var()}")
print(f"Desvio padrão: {df['salario'].std()}")
print(f"Moda: {df['salario'].mode()[0]}")
print(f"Minimo: {df['salario'].min()}")
print(f"Quartis: {df['salario'].quantile([0.25, 0.5, 0.75])}")
print(f"Maximo: {df['salario'].max()}")
print(f"Contagem de não nulos: {df['salario'].value_counts().sum()}")
print(f"Soma: {df['salario'].sum()}")

#Estrutura de dados
print(f"\nColuna do DataFrame:\n{df['salario']}")
print(f"Array do campo: {df['salario'].values}")

array_campo = df['salario'].values
print("Estatística com Numpy")
print(f"Média: {np.mean(array_campo)}")
print(f"Mediana: {np.median(array_campo)}")
print(f"Variancia: {np.var(array_campo)}")
print(f"Desvio padrão: {np.std(array_campo)}")
print(f"Minimo: {np.min(array_campo)}")
print(f"Quartis: {np.quantile(array_campo, [0.25, 0.5, 0.75])}")
print(f"Porcentagem: {np.percentile(array_campo, [25, 50, 75])}")
print(f"Maximo: {np.max(array_campo)}")
print(f"Contagem de não nulos: {np.count_nonzero(array_campo)}")
print(f"Soma: {np.sum(array_campo)}")