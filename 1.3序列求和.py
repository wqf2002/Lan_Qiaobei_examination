# 求1+2+3+…+n的值


import time  # 此行代码只用来测算时间与实际代码运行毫无关系

n = int(input())
a = time.time()  # 此行代码只用来测算时间与实际代码运行毫无关系
s = n * (n + 1) / 2
print('%d' % s)
b = time.time()  # 此行代码只用来测算时间与实际代码运行毫无关系
print(b - a)

# *******************************分割线*********************************

# sum_ = 0
# n = int(input())
# a = time.time()   # 此行代码只用来测算时间与实际代码运行毫无关系
# for i in range(0, n + 1):
#     sum_ += i
#     b = time.time()   # 此行代码只用来测算时间与实际代码运行毫无关系
# print(sum_)
# print(b - a)
