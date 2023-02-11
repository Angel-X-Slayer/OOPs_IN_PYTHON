n=int(input("enter the number : "))
class Finding_number:
    def __init__(self,number):
        self.check=number
    def checking_the_number(self):
        if(self.check==0):
            print("the number is 0")
        elif(self.check<0):
            print("the number is negetive")
        else:
            print("the number is positive")

a= Finding_number(n)
a.checking_the_number()