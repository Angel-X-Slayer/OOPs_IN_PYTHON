def reverse_string(idx, strng, arr):
    if idx < 0:
        return (arr)
    arr.append(strng[idx])
    idx -= 1
    return (reverse_string(idx, strng, arr))


strng = input("enter the string: ")
arr = []
k = reverse_string(len(strng)-1, strng, arr)
k = "".join(k)
print(k)
