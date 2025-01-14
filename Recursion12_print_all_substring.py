def print_substring(str, idx, op, ans):
    if idx == len(str):
        op1 = op.copy()
        ans.append(op1)
        return
    else:
        print_substring(str, idx+1, op, ans)
        op.append(str[idx])
        print_substring(str, idx+1, op, ans)
        op.pop()
    return (ans)


str = "abc"
idx = len(str)
op = []
ans = []
k = print_substring(str, 0, op, ans)
print(*(i for i in k))

# def greet(fx):
#     #   def mfx(*args, **kwargs):
#     print("Good Morning")
#     fx()
#     print("Thanks for using this function")
# #   return mfx


# @greet
# def hello():
#     print("Hello world")

# # @greet
# # def add(a, b):
# #   print(a+b)


# # greet(hello)()
# greet(hello)()
