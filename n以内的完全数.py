# 求n以内的完全数并输出他们的个数
def isp(n):
    m = True
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    if s != n:
        m = False
    return m


N = eval(input())

count = 0
for i in range(1, N + 1):
    if isp(i):
        count += 1
        print(i)
print(count)
