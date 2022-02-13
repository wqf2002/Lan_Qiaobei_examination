"""
输入两个整数a和b，输出这两个整数的和。a和b都不超过100位。
"""


def same_length(arr, long):
    arr = '0' * (long - len(arr)) + arr
    return arr


arr_1 = input()
arr_2 = input()
if len(arr_1) > len(arr_2):
    arr_2 = same_length(arr_2, len(arr_1))
elif len(arr_2) > len(arr_1):
    arr_1 = same_length(arr_1, len(arr_2))
print(arr_1)
print(arr_2)
result = [0 for i in range(len(arr_1) + 1)]
k = 0
for i in range(len(arr_1)):
    end = k + int(arr_1[len(arr_1) - i - 1]) + int(arr_2[len(arr_2) - i - 1])
    result[len(arr_1) - i] = end % 10
    k = 0
    if end >= 10:
        k = int(end / 10)

