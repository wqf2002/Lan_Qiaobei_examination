# Fibonacci数列的递推公式为：Fn=Fn-1+Fn-2，其中F1=F2=1。
# 当n比较大时，Fn也非常大，现在我们想知道，Fn除以10007的余数是多少。


n = int(input())
Fib = [1 for i in range(n + 1)]
k = 3
while k <= n:
    Fib[k] = (Fib[k - 1] + Fib[k - 2]) % 10007
    k += 1
print(Fib[n])