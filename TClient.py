from tinkoff.invest import Client, AccountType, AccountStatus

class TClient:

    def __init__(self, token):
        self.token = token

    def connect(self):
        self.client = (Client(self.token).__enter__())
        self.accounts = self.client.users.get_accounts().accounts
        self.portfolios = []
        for account in self.accounts:
            if (account.type in [AccountType.ACCOUNT_TYPE_TINKOFF,
                                AccountType.ACCOUNT_TYPE_TINKOFF_IIS]
                    and account.status == AccountStatus.ACCOUNT_STATUS_OPEN):
                self.portfolios += [self.client.operations.get_portfolio(account_id=account.id)]
