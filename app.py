import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go

from payoff import calculate_payoff
from charts import payoff_chart, historical_chart

st.set_page_config(layout="wide")

st.title("Lâmina de Estrutura de Derivativos Agrícolas")

# --------------------------------
# INPUTS
# --------------------------------

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

# --------------------------------
# TICKERS
# --------------------------------

tickers = {
    "Soja CBOT": "ZS=F",
    "Milho CBOT": "ZC=F"
}

ticker = tickers[ativo]

# --------------------------------
# DADOS DE MERCADO
# --------------------------------

data = yf.download(ticker, period="6mo", auto_adjust=True)

if data.empty:

    st.error("Erro ao carregar dados do Yahoo Finance.")
    st.stop()

preco_atual = float(data["Close"].iloc[-1])

# --------------------------------
# PAYOFF
# --------------------------------

prices, results, breakeven = calculate_payoff(
    estrutura,
    strike1,
    strike2,
    strike3,
    custo
)

# --------------------------------
# LAYOUT PRINCIPAL
# --------------------------------

col1, col2 = st.columns([1,2])

# --------------------------------
# COLUNA ESQUERDA
# --------------------------------

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
            "Preço Atual",
            "Breakeven"
        ],

        "Valor":[
            ativo,
            estrutura,
            strike1,
            strike2,
            strike3,
            custo,
            round(preco_atual,2),
            round(breakeven,2)
        ]

    })

    st.table(tabela)

# --------------------------------
# PAYOFF
# --------------------------------

with col2:

    st.subheader("Payoff da Estrutura")

    fig_payoff = payoff_chart(prices, results)

    st.plotly_chart(fig_payoff, use_container_width=True)

# --------------------------------
# HISTÓRICO + STRIKES
# --------------------------------

st.subheader("Histórico do Ativo + Strikes")

fig_hist = historical_chart(data, strike1, strike2, strike3)

st.plotly_chart(fig_hist, use_container_width=True)

# --------------------------------
# CANDLESTICK YAHOO FINANCE
# --------------------------------

st.subheader("Gráfico Candlestick (Yahoo Finance)")

fig_candle = go.Figure()

fig_candle.add_trace(
    go.Candlestick(
        x=data.index,
        open=data["Open"],
        high=data["High"],
        low=data["Low"],
        close=data["Close"],
        name="Preço"
    )
)

fig_candle.update_layout(
    title=f"{ativo} - Últimos 6 meses",
    xaxis_title="Data",
    yaxis_title="Preço",
    height=500,
    template="plotly_white"
)

st.plotly_chart(fig_candle, use_container_width=True)

# --------------------------------
# SIMULAÇÃO DE CENÁRIOS
# --------------------------------

st.subheader("Simulação de Cenários")

cenarios = [-0.20,-0.10,0,0.10,0.20]

resultados = []

for c in cenarios:

    preco = preco_atual * (1+c)

    payoff = np.interp(preco, prices, results)

    resultados.append({
        "Cenário": f"{int(c*100)}%",
        "Preço": round(preco,2),
        "Resultado": round(payoff,2)
    })

df = pd.DataFrame(resultados)

st.table(df)
