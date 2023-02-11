n=int(input("enter the number : "))
class Sum:
    def __init__(self,number):
        self.number=number
    def checking(self):
        s=0
        k=self.number
        while(self.number!=0):
            r=int(self.number%10)
            self.number=(self.number/10)
            s=s+r
        print(f"the sum of all the digits of the number {k} is {s}")

a=Sum(n)
a.checking()
