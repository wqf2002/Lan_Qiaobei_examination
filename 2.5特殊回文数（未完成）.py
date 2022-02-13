# 123321是一个非常特殊的数，它从左边读和从右边读是一样的。
# 输入一个正整数n， 编程求所有这样的五位和六位十进制数，满足各位数字之和等于n 。
import time


def is_pal(i):
    i_s = str(i)
    if i_s == i_s[::-1]:
        return True
    else:
        return False


def sum_i(i):
    s = 0
    i_s = str(i)
    for j in range(len(i_s)):
        s += int(i_s[j])
    return s


n = int(input())
start = time.time()
i = 10000
while i < 1000000:
    if is_pal(i):
        if sum_i(i) == n:
            print(i)
    i += 1
end = time.time()
print(end - start)
