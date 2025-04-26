import plotly.express as px
import pandas as pd

def plot_total_sales(df: pd.DataFrame, title: str):
    fig = px.bar(
        df,
        x="Vendedor",
        y="Valor Dia",
        color="Forma de Pagamento",
        template="plotly_dark",
        barmode="relative",
        text="Valor Dia",
        height=500,
        title=title
    )
    fig.update_layout(bargap=0.1)
    fig.update_traces(texttemplate="R$%{text},00", textposition="outside")
    return fig

def plot_quantity_by_payment(df: pd.DataFrame, title: str):
    fig = px.bar(
        df,
        x="Quantidade",
        y="Vendedor",
        color="Forma de Pagamento",
        orientation="h",
        barmode="stack",
        template="plotly_dark",
        labels={'Forma de Pagamento': 'Tipo de Pagamento', 'Quantidade': 'Quantidade de Vendas'},
        title=title
    )
    fig.update_layout(bargap=0.1)
    fig.update_traces(texttemplate='%{x}', textposition='inside')
    return fig

def plot_sales_per_vendor(df: pd.DataFrame, title: str):
    fig = px.bar(
        df,
        x="Quantidade",
        y="Vendedor",
        orientation="h",
        title=title,
        labels={'Vendedor': 'Vendedor', 'Quantidade': 'Quantidade de Vendas'}
    )
    fig.update_layout(bargap=0.1)
    fig.update_traces(texttemplate='%{x}', textposition='outside')
    return fig

def plot_pie_ranking(df: pd.DataFrame, values_col: str, names_col: str, title: str):
    fig = px.pie(
        df,
        values=values_col,
        names=names_col,
        title=title
    )
    fig.update_traces(textinfo='percent+label')
    return fig