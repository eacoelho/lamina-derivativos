import plotly.graph_objects as go

def payoff_chart(prices, results):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=prices,
            y=results,
            mode="lines",
            name="Payoff"
        )
    )

    fig.add_hline(y=0)

    fig.update_layout(
        title="Payoff da Estrutura",
        xaxis_title="Preço do Ativo",
        yaxis_title="Resultado"
    )

    return fig


def historical_chart(data, strike1, strike2, strike3):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["Close"],
            name="Preço"
        )
    )

    fig.add_hline(y=strike1)
    fig.add_hline(y=strike2)
    fig.add_hline(y=strike3)

    fig.update_layout(
        title="Histórico + Strikes"
    )

    return fig
