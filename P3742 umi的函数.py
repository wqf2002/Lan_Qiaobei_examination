def f(s1, s2, x):
    g = [0 for x in range(x)]
    for i in range(x):
        if s1[i] < s2[i]:
            return -1
        else:
            g[i] = min(s1[i], s2[i])
    return ''.join(map(str, g))


n = int(input())
str1 = str(input())
str2 = str(input())
print(f(str1, str2, n))
