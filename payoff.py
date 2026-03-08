import numpy as np

def calculate_payoff(estrutura, strike1, strike2, strike3, custo):

    prices = np.linspace(strike1*0.6, strike3*1.4, 200)

    if estrutura == "Long Put":

        payoff = np.maximum(strike1 - prices,0) - custo

    elif estrutura == "Long Call":

        payoff = np.maximum(prices - strike1,0) - custo

    elif estrutura == "Long Put Spread":

        payoff = (
            np.maximum(strike1 - prices,0)
            - np.maximum(strike2 - prices,0)
            - custo
        )

    elif estrutura == "Long Call Spread":

        payoff = (
            np.maximum(prices - strike1,0)
            - np.maximum(prices - strike2,0)
            - custo
        )

    elif estrutura == "Zero Cost Collar":

        payoff = (
            np.maximum(strike1 - prices,0)
            - np.maximum(prices - strike2,0)
            - custo
        )

    elif estrutura == "Seagull":

        payoff = (
            np.maximum(strike1 - prices,0)
            - np.maximum(prices - strike2,0)
            + np.maximum(prices - strike3,0)
            - custo
        )

    return prices, payoff
