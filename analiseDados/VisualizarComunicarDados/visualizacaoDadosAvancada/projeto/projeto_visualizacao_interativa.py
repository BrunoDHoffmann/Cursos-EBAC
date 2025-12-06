import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Output, Input
import math

df = pd.read_csv(r'D:\GitHub\Cursos-EBAC\analiseDados\VisualizarComunicarDados\visualizacaoDadosAvancada\projeto\ecommerce_estatistica (1).csv')
df.describe()

df['nota_arredondada'] = df['Nota'].apply(lambda x: math.trunc(x) if x >= 1 else 1)    
lista_notas = df['nota_arredondada'].unique()
options = [{'label': f'{nota} Estrela', 'value': nota} for nota in lista_notas]

def cria_graficos(selecao_checklist):
    filtro_df = df[df['nota_arredondada'].isin(selecao_checklist)]
    fig1 = px.bar(filtro_df, x='Nota', y='N_Avaliações', color='Desconto', barmode='group')
    fig1.update_layout(
        title='Grafico Nota vs Numero de avaliações e Desconto'
    )
    return fig1

def cria_app():
    app = Dash(__name__)
    app.layout = html.Div([
        html.H1('Projeto Dashboard Interativo'),
        html.P('Esse Dashboard ira apresentar os principais graficos usados para visualização avançada e diferentes tipos de interações.'),
        html.Br(),
        html.H2('Grafico de Barras'),
        dcc.Checklist(
            id = 'id_checklist',
            options = options,
            value = [lista_notas[0]]
        ),
        dcc.Graph(id='id_grafico_barras')
    ])
    return app

if __name__ == '__main__':
    app = cria_app()

    @app.callback(
        [Output('id_grafico_barras', 'figure')],
        [Input('id_checklist', 'value')]
    )
    def atualiza_grafico(selecao_checklist):
        fig1 = cria_graficos(selecao_checklist)
        return [fig1]

    app.run(debug=True, port=8050)