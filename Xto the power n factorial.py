# METHOD 1   (Height of Stack -> n)


# def find_power(x, n):
#     if x == 0 and n == 0:
#         return (None)
#     elif x == 0:
#         return 0
#     elif n == 0:
#         return 1
#     else:
#         return (x*find_power(x, n-1))


# x = int(input())
# n = int(input())
# ans = find_power(x, n)
# if ans == None:
#     print("Undefined")
# else:
#     print(ans)


###############################################################################


# METHOD 2  (Height of Stack -> log(n))


def find_power_1(x, n):
    if x == 0 and n == 0:
        return (None)
    elif x == 0:
        return 0
    elif n == 0:
        return 1
    else:
        if n % 2 == 0:
            return (find_power_1(x, int(round(n/2)))*find_power_1(x, int(round(n/2))))
        else:
            return (find_power_1(x, int(round(n/2)))*find_power_1(x, int(round(n/2)))*x)


x = int(input())
n = int(input())
ans = find_power_1(x, n)
if ans == None:
    print("Undefined")
else:
    print(ans)


##############################################################################
