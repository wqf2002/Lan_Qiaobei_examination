n, m = map(int, input().split())
graph = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        if j >= i:
            graph[i][j] = chr(ord('A') + j - i)
        else:
            graph[i][j] = chr(ord('A') + i - j)
for i in range(n):
    for j in range(m):
        print(graph[i][j], end='')
    print()
