class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(amount):
        print('Deposit Accepted')
        return (self.balance + amount)

    def withdrawl(amount):
        if self.balance < amount:
            return ('Funds Unavailable!')
        else:
            print('Withdrawal Accepted')
            return self.balance - amount

    def __str__(self):
        print(f'Account Owner: {self.owner} Account Balance: {self.balance}')


acct1 = Account('Jose', 200)

print(acct1)
