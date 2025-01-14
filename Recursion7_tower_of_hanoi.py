# def tower_of_hanoi(n, s, d, h):
#     if n == 1:
#         print(f"{n} disk from {s} to {d}")
#         print()
#         return
#     tower_of_hanoi(n-1, s, h, d)
#     print(f"{n} disk from {s} to {d}")
#     print()
#     tower_of_hanoi(n-1, h, d, s)

# tower_of_hanoi(3, "Source", "Destination", "Helper")       


# Both are working


def tower_of_hanoi(n, s, d, h):
    if n == 1:
        print(f"{n} disc transferred from {s} to {d}")
        print()
        return
    else:
        tower_of_hanoi(n-1, s, h, d)
        print(f"{n} disk transferred from {s} to {d}")
        print()
        tower_of_hanoi(n-1, h, d, s)


tower_of_hanoi(5, "Source", "Destination", "Helper")
