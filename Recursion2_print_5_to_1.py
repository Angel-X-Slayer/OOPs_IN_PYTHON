def printing(i):
    if i == 0:
        return
    else:
        print(i, end=" ")
        printing(i-1)


n = int(input("enter a number: "))
printing(n)
