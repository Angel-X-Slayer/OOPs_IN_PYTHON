class credit_card:
    def __init__(self, cust, bnk, acnt, lmt):
        self.customer = cust
        self.bank = bnk
        self.account = acnt
        self.limit = lmt
        self.balance = 0000000

    def Get_Customer(self):
        print(self.customer)

    def Get_Bank(self):
        print(self.bank)

    def Get_Account(self):
        print(self.account)

    def Get_Balance(self):
        # self.balance = bal
        print(self.balance)

    def Get_Limit(self):
        print(self.limit)

    def Charge(self, price, amount):
        if price+self.balance > self.limit:
            print("exceeds the limit,cannot do the transaction")
        else:
            print("precessing")
            self.balance -= amount
            print(self.balance)


# bal = int(input("enter the balance: "))
price = int(input("enter the price: "))
amount = int(input("enter the amount: "))
cc = credit_card("John Wick", "Bank Of Mafia", "SAVINGS" "1000", 90)
cc.Get_Account()
cc.Get_Balance()
cc.Get_Customer()
cc.Get_Limit()
cc.Get_Bank()
cc.Charge(price, amount)
# if __name__=='__main__':
#     wallet=[]
