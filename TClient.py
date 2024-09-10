from tinkoff.invest import Client, AccountType, AccountStatus

class TClient:
    def __init__(self, token: str):
        self.client = (Client(token).__enter__())
        self.accounts = self.client.users.get_accounts().accounts

        self.portfolios = []
        for account in self.accounts:
            if (account.type in [AccountType.ACCOUNT_TYPE_TINKOFF,
                                AccountType.ACCOUNT_TYPE_TINKOFF_IIS]
                    and account.status == AccountStatus.ACCOUNT_STATUS_OPEN):
                self.portfolios += [self.client.operations.get_portfolio(account_id=account.id)]


class TMergeClient:
    def __init__(self, tokens:[str]):
        self.t_clients = [TClient(token) for token in tokens]

        self.accounts = []
        self.portfolios = []

        for t_client in self.t_clients:
            self.accounts += t_client.accounts
            self.portfolios += t_client.portfolios