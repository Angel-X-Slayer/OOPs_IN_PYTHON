# If you want to return the value from the recursive function to the main function
def print_factorial(n, fact):
    if n == 0:
        return fact
    else:
        fact *= n
        return (print_factorial(n-1, fact))


n = int(input("enter the number: "))
print(print_factorial(n, 1))


# If you want to print the value from the recursive function
def print_factorial(n, fact):
    if n == 0:
        print(fact)
        return
    else:
        fact *= n
        print_factorial(n-1, fact)


n = int(input("enter the number: "))
print_factorial(n, 1)
