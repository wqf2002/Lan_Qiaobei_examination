"""
输入一个正整数n，输出n!的值。其中n!=123*…*n。
"""

n = int(input())
a = s = 1
while a <= n:
    s *= a
    a += 1
print(s)
