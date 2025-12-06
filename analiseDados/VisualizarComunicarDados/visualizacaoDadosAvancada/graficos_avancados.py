import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

df=pd.read_csv(r'D:\GitHub\Cursos-EBAC\analiseDados\VisualizarComunicarDados\matematicaEstatistica\estatisticaBasica\clientes-v3-preparado.csv')

def cria_grafico(df):
    # Histograma
    fig1 = px.histogram(df, x='salario', nbins=30, title='Distribuição de Salários')

    # Grafico de pizza
    fig2 = px.pie(df, names='area_atuacao', color='area_atuacao', hole=0.2, color_discrete_sequence=px.colors.sequential.RdBu)

    # Grafico de Bolhas
    fig3 = px.scatter(df, x='idade', y='salario', size='anos_experiencia', color='area_atuacao', hover_name='estado', size_max=60)
    fig3.update_layout(title='Salario por Idade e Anos de Experiencia')

    # Grafico de Linhas
    fig4 = px.line(df, x='idade', y='salario', color='area_atuacao', facet_col='nivel_educacao')
    fig4.update_layout(
        title='Salario por Idade e Area de Atuacao para cada Nivel de Educação',
        xaxis_title='Idade',
        yaxis_title='Salario'
    )

    # Grafico #3D
    fig5 = px.scatter_3d(df, x='idade', y='salario', z='anos_experiencia', color='nivel_educacao')

    # Grafico de barra
    fig6 = px.bar(df, x='estado_civil', y='salario', color='nivel_educacao', barmode='group', color_discrete_sequence=px.colors.sequential.RdBu)
    fig6.update_layout(
        title='Salario por Estado Civil e Nivel de Educação',
        xaxis_title='Estado Civil',
        yaxis_title='Salario',
        legend_title='Nivel de Educação',
        plot_bgcolor='rgba(222, 255, 253, 1)',
        paper_bgcolor='rgba(186, 245, 241, 1)'
    )
    return fig1, fig2, fig3, fig4, fig5, fig6

# Criar App
def cria_app(df):
    app = Dash(__name__)

    fig1, fig2, fig3, fig4, fig5, fig6 = cria_grafico(df)

    app.layout = html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig5),
        dcc.Graph(figure=fig6)
    ])
    return app

# Executa App
if __name__ == '__main__':
    app = cria_app(df)
    app.run(debug=True, port=8050) # Default 8050