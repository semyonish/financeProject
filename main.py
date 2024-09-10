from TClient import TClient, TMergeClient
from tokens import TOKENS
from useful_functions import accounts_dataframe, positions_df

if __name__ == '__main__':
    client = TMergeClient(TOKENS)

    print(accounts_dataframe(client.accounts))

    print(positions_df(client.portfolios[0].positions))




