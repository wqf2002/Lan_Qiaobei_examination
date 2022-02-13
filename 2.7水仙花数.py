def is_nar(i_):
    a = i_ % 10  # 十位
    b = int(i_ / 10) % 10  # 百位 注意Python中除法一定会得到浮点数 要取整 而C中则不需要
    c = int(i_ / 100)
    if i_ == a ** 3 + b ** 3 + c ** 3:
        return True
    else:
        return False


i = 100
while i < 1000:
    if is_nar(i):
        print(i)
    i += 1
