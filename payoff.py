import numpy as np

def calculate_payoff(estrutura, strike1, strike2, strike3, custo):

    max_strike = max(strike1, strike2, strike3)

    prices = np.linspace(max_strike * 0.6, max_strike * 1.4, 300)

    if estrutura == "Long Put":

        payoff = np.maximum(strike1 - prices, 0) - custo

    elif estrutura == "Long Call":

        payoff = np.maximum(prices - strike1, 0) - custo

    elif estrutura == "Long Put Spread":

        payoff = (
            np.maximum(strike1 - prices, 0)
            - np.maximum(strike2 - prices, 0)
            - custo
        )

    elif estrutura == "Long Call Spread":

        payoff = (
            np.maximum(prices - strike1, 0)
            - np.maximum(prices - strike2, 0)
            - custo
        )

    elif estrutura == "Zero Cost Collar":

        payoff = (
            np.maximum(strike1 - prices, 0)
            - np.maximum(prices - strike2, 0)
            - custo
        )

    elif estrutura == "Seagull":

        payoff = (
            np.maximum(strike1 - prices, 0)
            - np.maximum(prices - strike2, 0)
            + np.maximum(prices - strike3, 0)
            - custo
        )

    else:

        payoff = np.zeros_like(prices)

    # cálculo aproximado de breakeven
    idx = np.argmin(np.abs(payoff))
    breakeven = prices[idx]

    return prices, payoff, breakeven
