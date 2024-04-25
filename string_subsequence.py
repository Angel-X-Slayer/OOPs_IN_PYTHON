def subsequence(arr,i,resultant):
    if (i==len(arr)):
        print(resultant)
        return
    current=arr[i]
    subsequence(arr,i+1,resultant+current)
    subsequence(arr,i+1,resultant)
    pass

arr="abcd"
subsequence(arr,0,"")