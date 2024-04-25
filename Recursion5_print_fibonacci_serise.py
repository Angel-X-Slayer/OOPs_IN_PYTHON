# Solution 1

def printfib(i, arr, idx):
    if idx == i:
        return (arr)
    else:
        arr.append(arr[idx-1]+arr[idx-2])
        idx += 1
        return (printfib(i, arr, idx))


n = int(input("enter the number: "))
arr = []
arr.append(0)
arr.append(1)
print(printfib(n, arr, idx=2))


# Solution 2
def printfib(i, arr, idx):
    if idx == i:
        return (arr)
    else:
        arr[idx] = (arr[idx-1]+arr[idx-2])
        idx += 1
        return (printfib(i, arr, idx))


n = int(input("enter the number: "))
arr = [None]*n
arr[0] = 1
arr[1] = 1
print(printfib(n, arr, idx=2))
