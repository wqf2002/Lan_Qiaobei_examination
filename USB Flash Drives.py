n = int(input())
m = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
sum_s = 0
num = 0
for i in a:
    if sum_s < m:
        sum_s += i
        num += 1
    else:
        break
print(num)