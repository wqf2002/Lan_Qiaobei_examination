def is_pal(i_):
    i_s = str(i_)
    if i_s == i_s[::-1]:
        return True
    else:
        return False


i = 1
while True:
    if is_pal(i):
        print(i)
    i += 1
