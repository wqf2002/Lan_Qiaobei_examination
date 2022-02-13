# 给出一个包含n个整数的数列，问整数a在数列中的第一次出现是第几个。
n = int(input())
arr = input().split()
a = input()
i = 0
while i < n:
    if a == arr[i]:
        print(i+1)
        break
    i += 1
if i == n:
    print(-1)