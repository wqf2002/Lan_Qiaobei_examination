n = int(input())
arr = list(map(int, input().split()))
price = [0 for i in range(n - 1)]
for i in range(n - 1):
    arr.sort()
    value = arr.pop(0)
    value_2 = arr.pop(0)
    price[i] = value + value_2
    arr.append(price[i])
print(sum(price))
