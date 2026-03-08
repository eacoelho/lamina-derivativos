import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf

from payoff import calculate_payoff
from charts import payoff_chart, historical_chart

st.set_page_config(layout="wide")

st.title("Lâmina de Estrutura de Derivativos Agrícolas")

# -------------------------
# Inputs
# -------------------------

ativo = st.selectbox(
    "Ativo",
    ["Soja CBOT", "Milho CBOT"]
)

estrutura = st.selectbox(
    "Estrutura",
    [
        "Long Put",
        "Long Call",
        "Long Put Spread",
        "Long Call Spread",
        "Zero Cost Collar",
        "Seagull"
    ]
)

strike1 = st.number_input("Strike 1", value=100.0)
strike2 = st.number_input("Strike 2", value=110.0)
strike3 = st.number_input("Strike 3", value=120.0)

custo = st.number_input("Custo da Estrutura", value=0.0)

# -------------------------
# Tickers
# -------------------------

tickers = {

    "Soja CBOT": "ZS=F",
    "Milho CBOT": "ZC=F"

}

ticker = tickers[ativo]

# -------------------------
# Dados de mercado
# -------------------------

data = yf.download(ticker, period="6mo")

if data.empty:

    st.error("Não foi possível carregar dados de mercado.")
    st.stop()

preco_atual = float(data["Close"].iloc[-1])

# -------------------------
# Payoff
# -------------------------

prices, results = calculate_payoff(
    estrutura,
    strike1,
    strike2,
    strike3,
    custo
)

# -------------------------
# Layout
# -------------------------

col1, col2 = st.columns([1,2])

with col1:

    st.subheader("Características da Estrutura")

    tabela = pd.DataFrame({

        "Parâmetro":[
            "Ativo",
            "Estrutura",
            "Strike 1",
            "Strike 2",
            "Strike 3",
            "Custo",
            "Preço Atual"
        ],

        "Valor":[
            ativo,
            estrutura,
            strike1,
            strike2,
            strike3,
            custo,
            round(preco_atual,2)
        ]

    })

    st.table(tabela)

with col2:

    st.subheader("Payoff da Estrutura")

    fig = payoff_chart(prices, results)
    st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Histórico
# -------------------------

st.subheader("Histórico do Contrato (6 meses)")

fig2 = historical_chart(data, strike1, strike2, strike3)

st.plotly_chart(fig2, use_container_width=True)

# -------------------------
# Gráfico Yahoo Finance
# -------------------------

st.subheader("Gráfico do Ativo (Yahoo Finance)")

import plotly.graph_objects as go

fig3 = go.Figure()

fig3.add_trace(
    go.Candlestick(
        x=data.index,
        open=data["Open"],
        high=data["High"],
        low=data["Low"],
        close=data["Close"],
        name="Preço"
    )
)

fig3.update_layout(
    title=f"{ativo} - Últimos 6 meses",
    xaxis_title="Data",
    yaxis_title="Preço",
    height=500
)

st.plotly_chart(fig3, use_container_width=True)
