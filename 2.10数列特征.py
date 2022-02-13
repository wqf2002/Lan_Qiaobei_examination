# 给出n个数，找出这n个数的最大值，最小值，和。
n = int(input())
arr = input().split()
print(max(int(arr[i])for i in range(n)))
print(min(int(arr[i])for i in range(n)))
print(sum(int(arr[i])for i in range(n)))
