import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('D:/GitHub/Cursos-EBAC/VisualizarComunicarDados/matematicaEstatistica/estatisticaBasica/clientes-v3-preparado.csv')

x = df['nivel_educacao'].value_counts().index
y = df['nivel_educacao'].value_counts().values

# Grafico de Barras
plt.figure(figsize=(10, 6))
plt.bar(x, y, color='#60aa65')
plt.title('Divisao de escolaridade')
plt.xlabel('Nivel educação')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)

# Grafico de Pizza
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Distribuição de Nivel de Educação')

# Grafico de Dispersão
plt.figure(figsize=(10, 6))
plt.hexbin(df['idade'], df['salario'], gridsize=40, cmap='Blues')
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('Idade')
plt.ylabel('Salario')
plt.title('Dispersão de Idade e Salario')
plt.show()