n=int(input("enter the value :"))
m=int(input("enter the value :"))
class add:
    def __init__(self,number1,number2):
        self.addendum1=number1
        self.addendum2=number2
    def addition(self):
        c=self.addendum1+self.addendum2
        print("the sum is",c)


a=add(n,m)
a.addition()