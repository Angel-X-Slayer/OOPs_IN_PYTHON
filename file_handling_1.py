# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([0, 10])
# ypoints = np.array([0, 250])
# print(xpoints)

# plt.plot(xpoints, ypoints)
# plt.show()
#############################################################################################################
# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([1, 2, 6, 10000])
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(xpoints, ypoints)
# plt.show()
##############################################################################################################
# import matplotlib.pyplot as plt

# x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]
# y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
# classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]

# plt.scatter(x, y, c=classes)
# plt.show()
##############################################################################################################
# format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"

# print("Int formatting:", format_numeric(1000000))
# print("float formatting:", format_numeric(999999.789541235))
##############################################################################################################

is_even_list = [lambda arg=x: (arg* 10) for x in range(1, 5)]
 
# iterate on each lambda function
# and invoke the function to get the calculated value
for item in is_even_list:
    print(item())

