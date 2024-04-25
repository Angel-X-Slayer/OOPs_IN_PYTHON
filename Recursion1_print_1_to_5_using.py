def printing(i, n):
    if i == n:
        print(i)
        return
    else:
        print(i)
        i += 1
        printing(i, n)


n = int(input("enter the last number :"))
printing(1, n)
