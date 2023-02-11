class credit_card:
    def __init__(self,cust,bnk,acnt,lmt):
        self.customer=cust
        self.bank=bnk
        self.account=acnt
        self.limit=lmt
        self.balance=0000000
    def Get_Customer(self):
        print(self.customer)
    def Get_Bank(self):
        print(self.bank)
    def Get_Account(self):
        print(self.account)
    def Get_Balance(self,bal):
        self.balance=bal
        print(self.balance)
    def Get_Limit(self):
        print(self.limit)
    def Charge(self,price,amount):
        if price+self.balance>self.limit:
            print("exceeds the limit,cannot do the transaction")
        else:
            print("precessing")
            self.balance-=amount
            print(self.balance)

cc=credit_card("John Wick","Bank Of Leora","11700319003",100000000)
bal=int(input("enter the balance: "))
price=int(input("enter the price: "))
amount=int(input("enter the amount: "))
cc.Get_Account()
cc.Get_Balance(bal)
cc.Get_Customer()
cc.Get_Limit()
cc.Get_Bank()
cc.Charge(price,amount)
# if __name__=='__main__':
#     wallet=[]
    


