import streamlit as st
from dashboard import loaders, preprocessors, charts, utils

# Initial setup
utils.set_locale()
st.set_page_config(layout="wide", initial_sidebar_state="expanded")
st.title('DASHBOARD DE CONTROLE')

# Sidebar
bar = st.sidebar
escolha = bar.selectbox("Escolha uma opção", ["Vendas Totais", "Produtos mais Vendidos"])

if escolha == "Vendas Totais":
    uploaded_file = st.file_uploader("Upload arquivo de Vendas (.xlsx)", type=["xlsx"], key="vendas")

    if uploaded_file:
        df = loaders.load_excel(uploaded_file)

        if "Valor" not in df.columns:
            bar.error("Arquivo inválido: coluna 'Valor' não encontrada.")
        else:
            df = preprocessors.preprocess_vendas(df)
            col1, col2 = st.columns(2)

            with bar:
                dias = df["Day"].unique().tolist()
                dia_selecionado = st.selectbox("Selecione o Dia", ["todos"] + dias)

            if dia_selecionado == "todos":
                fig = charts.plot_total_sales(df, "Vendas Totais (Todos os Dias)")
                st.plotly_chart(fig, use_container_width=True)
                st.dataframe(df, use_container_width=True)
            else:
                df_filtered = df[df["Day"] == dia_selecionado]
                fig = charts.plot_total_sales(df_filtered, f"Vendas Totais (Dia {dia_selecionado})")
                st.plotly_chart(fig, use_container_width=True)
                st.dataframe(df_filtered, use_container_width=True)

elif escolha == "Produtos mais Vendidos":
    uploaded_file = st.file_uploader("Upload arquivo de Produtos (.xlsx)", type=["xlsx"], key="produtos")

    if uploaded_file:
        df = loaders.load_excel(uploaded_file)

        if "Quantidade" not in df.columns:
            bar.error("Arquivo inválido: coluna 'Quantidade' não encontrada.")
        else:
            df = preprocessors.preprocess_produtos(df)
            col1, col2 = st.columns(2)

            with bar:
                dias = df["Day"].unique().tolist()
                dia_selecionado = st.selectbox("Selecione o Dia", ["todos"] + dias)

            if dia_selecionado == "todos":
                fig = charts.plot_sales_per_vendor(df, "Produtos Mais Vendidos (Todos os Dias)")
                st.plotly_chart(fig, use_container_width=True)
                st.dataframe(df, use_container_width=True)
            else:
                df_filtered = df[df["Day"] == dia_selecionado]
                fig = charts.plot_sales_per_vendor(df_filtered, f"Produtos Mais Vendidos (Dia {dia_selecionado})")
                st.plotly_chart(fig, use_container_width=True)
                st.dataframe(df_filtered, use_container_width=True)
