import pandas as pd

def preprocess_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(columns=["Nota Fiscal", "Cliente"], errors='ignore')
    df["Data"] = pd.to_datetime(df["Data"], dayfirst=True)
    df["Day"] = df["Data"].dt.day.astype(str)

    #Agrupar valor por dia e vendedor (gerar Valor Dia)
    soma_dia = df.groupby(["Day", "Vendedor"])["Valor"].sum().reset_index()
    soma_dia.rename(columns={"Valor": "Valor Dia"}, inplace=True)

    #Mesclar para adicionar "Valor Dia" no dataframe principal
    df = pd.merge(df, soma_dia, on=["Day", "Vendedor"], how="left")

    return df

def preprocess_produtos(df: pd.DataFrame) -> pd.DataFrame:
    df["Valor Total"] = df["Valor Total"].str.replace('R$ ', '').str.replace('.', '').str.replace(',', '.')
    df["Valor Total"] = df["Valor Total"].astype(float)
    df["Última Venda"] = pd.to_datetime(df["Última Venda"], dayfirst=True)
    df["Day"] = df["Última Venda"].dt.day.astype(str)
    return df
