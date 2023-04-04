# 贪心算法，排序
N, B = list(map(int, input().split()))
cow_height = []
sum_height = 0
sum_cow = 0
for i in range(N):
    cow_height.append(int(input()))
cow_height.sort(reverse=True)
for i in cow_height:
    if sum_height < B:
        sum_height += i
        sum_cow += 1
    else:
        print(sum_cow)
        break
