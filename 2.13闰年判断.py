"""
给定一个年份，判断这一年是不是闰年。当以下情况之一满足时，这一年是闰年：
1、年份是4的倍数而不是100的倍数；
2、年份是400的倍数。
"""


def is_leap_year(years):
    if years % 4 == 0 and years % 100 != 0 or years % 400 == 0:
        return True
    return False


year = int(input())
if is_leap_year(year):
    print('yes')
else:
    print('no')
