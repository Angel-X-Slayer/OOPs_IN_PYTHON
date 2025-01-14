# def printpower(x, n, pwr):
#     if n == 0:
#         return pwr
#     else:
#         pwr *= x*printpower(x, n-1, pwr)
#         return (pwr)


# x = int(input("enter the value of x: "))
# n = int(input("enter the value of n: "))
# pwr = 1
# print(printpower(x, n, pwr))


#  Solution 2
def printpower(x, n, pwr):
    if n == 0:
        return pwr
    else:
        rvalue = printpower(x, n-1, pwr)
        x *= rvalue
        return (x)


x = int(input("enter the value of x: "))
n = int(input("enter the value of n: "))
pwr = 1
print(printpower(x, n, pwr))
