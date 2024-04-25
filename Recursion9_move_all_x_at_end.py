def move_all_x(idx, strng, arr, count):
    if idx == len(strng):
        for i in range(count):
            arr.append("x")
        return arr
    else:
        if strng[idx] == "x" or strng[idx] == "X":
            count += 1
        else:
            arr.append(strng[idx])
    idx += 1
    return (move_all_x(idx, strng, arr, count))


strng = "abdjhgysjggfhasdxxhcxgxfxtyguixxxtgyuiyutrxhxyutxytuiox"
arr = []
k = move_all_x(0, strng, arr, 0)
k = "".join(k)
print(k)
