
# If you want to return the value from the recursive function to the main function
def summetion(i, n, sum):
    if i == n+1:
        return sum
    else:
        sum += i
        return (summetion(i+1, n, sum))


n = int(input("enter the number: "))
k = summetion(0, n, 0)
print(k)


# If you want to print the result in the recursive function
def summetion(i, n, sum):
    if i == n+1:
        print(sum)
        return
    else:
        sum += i
        summetion(i+1, n, sum)


n = int(input("enter the number: "))
summetion(0, n, 0)
