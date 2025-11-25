import pandas as pd

df = pd.read_csv('D:/GitHub/Cursos-EBAC/tratamentoDados/clientes-v2.csv')

print(df.head().to_string())
print(df.tail().to_string())
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

print('Verificação inicial: ')
print(df.info())

print(f'Analise de daados nulos: \n {df.isnull().sum()}')
print(f'% de dados nulos: \n {df.isnull().mean()*100}')
df.dropna(inplace=True)
print(f'Confirmar remoção de dados nulos: \n {df.isnull().sum().sum()}')

print(f'Analise de dados duplicados: \n {df.duplicated().sum()}')

print(f'Analise de dados unicos: \n {df.nunique()}')

print(f'Estatisticas dos dados: \n {df.describe()}')

df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]
print(df.head().to_string())

df.to_csv('clientes-v2-tratados.csv', index=False)