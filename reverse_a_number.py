class Sum:
    def __init__(self, number):
        self.number = number

    def reverse(self):
        k = self.number
        rev = 0
        while (self.number != 0):
            r = int(self.number % 10)
            rev = (rev*10)+r
            self.number = int(self.number/10)

        print(f"the reversed number is {rev}, the original number is {k}")


n = int(input("enter the number : "))
a = Sum(n)
a.reverse()
