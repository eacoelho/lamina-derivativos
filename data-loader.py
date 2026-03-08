import yfinance as yf

def carregar_dados(ticker):

    data = yf.download(
        ticker,
        period="6mo",
        interval="1d",
        auto_adjust=True,
        progress=False
    )

    return data
