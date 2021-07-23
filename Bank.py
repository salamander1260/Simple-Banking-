class Account:

    def __init__(self, owner, balance, savings):
        self.owner = owner
        self.balance = balance
        self.savings = savings

    def deposit(self, balance):
        self.balance = self.balance + balance
        print("{} added ${}".format(self.owner,balance))
        print("Now {} Total is ${}".format(self.owner,self.balance))

        return self.balance

    def withdrawl(self, balance):
        print("{} has ${} to withdrawal".format(self.owner, self.balance))
        self.balance = self.balance - balance
        print("{} withdrew ${}".format(self.owner, balance))
        print("Now {} Total is ${}".format(self.owner,self.balance))
        return self.balance

    def save(self, savings):
        self.savings = self.balance * .2
        print("With ${}, you could save ${}".format(self.balance, self.savings))
        return self.savings


acct1 = Account("Sala", 1000, 0)
# print(acct1.save(''))  # Checks how much/original savings
# print()
# print(acct1.deposit(800))  # add 800 into original balance
# print()
# print(acct1.save(''))  # Checks new balance multiply by 20% saving
# print()
# print(acct1.withdrawl(500))
#
# acct1.withdrawl(500)

acct1.deposit(1000)
print()
acct1.withdrawl(500)
print()
acct1.save('')