class Account:
    def __init__(self,cardno,pin,bal,withdrawal,acctype):
        self.cardno=cardno
        self.pin=pin
        self.bal=bal
        self.withdrawal=withdrawal
        self.acctype=acctype
    
    def update_withdrawal(self):
        if self.bal>=self.withdrawal:
            self.bal-=self.withdrawal

class ATM:
    def __init__(self,branchname,obj_list):
        self.breanchname=branchname
        self.obj_list=obj_list
    def 