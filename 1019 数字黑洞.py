'''
给定任一个各位数字不完全相同的 4 位正整数，如果我们先把 4 个数字按非递增排序，
再按非递减排序，然后用第 1 个数字减第 2 个数字，将得到一个新的数字。一直重复这样做，
我们很快会停在有“数字黑洞”之称的 6174，这个神奇的数字也叫 Kaprekar 常数。
'''
a = input()
if len(a) < 4:
    a = (4 - len(a)) * '0' + a
if a[0] == a[1] == a[2] == a[3]:
    print('{} - {} = {}'.format(a, a, '0000'))
    exit()
def f(n):
    n = ''.join(sorted(n))
    n1 = n[::-1]
    n2 = int(n1) - int(n)
    n2 = str(n2)
    if len(n2) < 4:
        n2 = (4 - len(n)) * '0' + n2
    print('{} - {} = {}'.format(n1, n, n2))
    if n2 == '6174':
        return 0
    else:
        f(n2)
f(a)