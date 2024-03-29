T, M = map(int, input().split())  # 传入数据
medicine_list = []
for _ in range(M):
    medicine_list.append(list(map(int, input().split())))

dp = [[0] * (T + 1) for _ in range(M + 1)]

for row in range(1, M + 1):
    for col in range(1, T + 1):
        time = medicine_list[row - 1][0]
        value = medicine_list[row - 1][1]
        if time > col:
            dp[row][col] = dp[row - 1][col]
        else:
            dp[row][col] = max(value + dp[row - 1][col - time], dp[row - 1][col])
print(dp[-1][-1])
