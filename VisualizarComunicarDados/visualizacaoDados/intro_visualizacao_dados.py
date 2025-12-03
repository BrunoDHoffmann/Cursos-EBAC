import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('D:/GitHub/Cursos-EBAC/VisualizarComunicarDados/matematicaEstatistica/estatisticaBasica/clientes-v3-preparado.csv')

#Histograma
plt.hist(df['salario'])
plt.show()

#Histograma - parametros
plt.figure(figsize=(10, 6))
plt.hist(df['salario'], bins=100, color='green', alpha=0.8)
plt.title('Histograma - Distribuição de Salario')
plt.xlabel('Salario')
plt.xticks(ticks=range(0, int(df['salario'].max())+2000, 2000))
plt.ylabel('Frequencia')
plt.grid(True)
plt.show()

# Multiplos graficos
# Grafico de dispersao
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1) # 2 Linhas, 2 Colunas, 1º grafico
plt.scatter(df['salario'], df['salario'])
plt.title('Dispersao - Salario e Salario')
plt.xlabel('Salario')
plt.ylabel('Salario')

plt.subplot(1, 2, 2) # 1 Linha, 2 Colunas, 2º grafico
plt.scatter(df['salario'], df['anos_experiencia'], color='#5883a8', alpha=0.6, s=30)
plt.title('Dispersao - Idade e Anos de experiencia')
plt.xlabel('Salario')
plt.ylabel('Anos de experiencia')

# Mapa de calor
corr = df[['salario', 'anos_experiencia']].corr()
plt.subplot(2, 2, 3) #2 Linhas, 2 Colunas, 3º
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Salario e Idade')

plt.tight_layout() # Ajustar espaçamentos
plt.show()