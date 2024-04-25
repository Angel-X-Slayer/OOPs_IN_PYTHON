def ifsorted(arr, idx, tag):
    if idx == len(arr)-1:
        return tag
    else:
        if arr[idx] < arr[idx+1]:
            tag = 1
            idx += 1
            return (ifsorted(arr, idx, tag))
        else:
            tag = 0
            return (tag)


arr = [5, 4, 3, 2, 1]
k = ifsorted(arr, 0, 0)
if k == 0:
    print("unsorted")
else:
    print("sorted")
