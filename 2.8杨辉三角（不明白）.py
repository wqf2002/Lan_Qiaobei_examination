n = int(input())

k = 2

triangle_yang = []  # 杨辉三角

for i in range(n):  # 定义空的杨辉三角
    triangle_yang.append([0 for j in range(i + 1)])

# print(triangle_yang)
# exit()
for i in range(n):  # 第一列和每一行的最后一个为1
    triangle_yang[i][0] = triangle_yang[i][-1] = 1

while k < n:
    m = 1
    while m < k:  # 两肩数值之和
        triangle_yang[k][m] = triangle_yang[k - 1][m - 1] + triangle_yang[k - 1][m]
        m += 1
    k += 1

for i in range(n):  # 输出杨辉三角
    for j in range(i + 1):
        print(triangle_yang[i][j], end=' ')
    print()
