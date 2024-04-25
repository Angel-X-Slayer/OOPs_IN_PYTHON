def remove_duplicates(strng, idx, out, str):
    if idx == len(strng):
        return str
    else:
        t = ord(strng[idx])-97
        if out[t] == 0:
            str += strng[idx]
            idx += 1
            out[t] = 1
            return (remove_duplicates(strng, idx, out, str))
        else:
            idx += 1
            return (remove_duplicates(strng, idx, out, str))


out = [0]*27
str = ""
strng = input("enter only small alphabet: ")
k = remove_duplicates(strng, 0, out, str)
print(k)


# if t < 97:
#     t -= 65

# else:
#     t -= 97
#     if out[t] == 0:
#         str += strng[idx]
#         idx += 1
#         out[t] = 1
#         return (remove_duplicates(strng, idx, out, str))
#     else:
#         idx += 1
#         return (remove_duplicates(strng, idx, out, str))
