import plotly.express as px
import pandas as pd
import plotly.io as pio
pio.renderers.default = "browser"

df = pd.read_csv(r'D:\GitHub\Cursos-EBAC\analiseDados\VisualizarComunicarDados\matematicaEstatistica\estatisticaBasica\clientes-v3-preparado.csv')

# Grafico de dispersao
fig = px.scatter(df, x='idade', y='salario', color='nivel_educacao', hover_data=['estado_civil'])
fig.update_layout(
    title='Idade Vs Salario por Nivel de Educação',
    xaxis_title='Idade',
    yaxis_title='Salario'
)
fig.show()