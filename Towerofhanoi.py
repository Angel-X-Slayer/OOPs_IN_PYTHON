def towerofhanoi(n, source, helper, destination):
    if (n == 1):
        print(f"disc {n} transfered from {source} to {destination}")
        return

    towerofhanoi(n-1, source, destination, helper)
    print(f"disc {n} transfered from {source} to {destination}")
    towerofhanoi(n-1, helper, source, destination)


n = int(input())
towerofhanoi(n, "Sorce", "Help", "Destination")
