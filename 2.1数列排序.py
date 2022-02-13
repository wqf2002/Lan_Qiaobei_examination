# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
# for i in range(n):
#     print(arr[i])

# *****************分割线********************************

# def list_sorted():
#     a = int(input())
#     b = input().split()
#     list1 = []
#     if a == len(b):
#         for i in range(a):
#             list1.append(int(b[i]))
#         list1.sort(reverse=False)
#         for num in list1:
#             print(num)
#
#
# list_sorted()

# ******************************分割线********************************

# def main():
#     lst1 = []
#     n = int(input())
#     lst2 = input().split()
#     for i in range(n):
#         lst1.append(int(lst2[i]))
#     lst1.sort()
#     for num in lst1:
#         print(num)
#
#
# main()

# *******************************分割线*************************

n = int(input())
a = list(map(int, input().split()))
a.sort()
for i in a:
    if n == 1:
        print('', end=str(i))
        break
    print(str(i), end=' ')
    n -= 1
