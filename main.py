from TClient import TMergeClient
from stats import Portfolio
from tokens import TOKENS

if __name__ == '__main__':
    client = TMergeClient(TOKENS)

    portfolio = Portfolio(client.portfolios)
    portfolio.print_info()
    portfolio.print_positions()
