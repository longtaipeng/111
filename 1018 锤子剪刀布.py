'''
输入第 1 行给出正整数 N（≤10​5​​），即双方交锋的次数。随后 N 行，
每行给出一次交锋的信息，即甲、乙双方同时给出的的手势。C 代表“锤子”、
J 代表“剪刀”、B 代表“布”，第 1 个字母代表甲方，第 2 个代表乙方，中间有 1 个空格。
'''

n = int(input())
a = {'win': [], 'win1': 0, 'lose': 0, 'ping': 0}
b = {'win': [], 'win1': 0, 'lose': 0, 'ping': 0}
k = {'C': 0, 'J': 1,  'B':2}
for i in range(n):
    A1, A2 = input().split(' ')
    if k[A1] - k[A2] == -1 or k[A1] - k[A2] == 2:
        a['win'].append(A1)
        a['win1'] += 1
        b['lose'] += 1
    elif k[A1] - k[A2] == -2 or k[A1] - k[A2] == 1:
        b['win'].append(A2)
        b['win1'] += 1
        a['lose'] += 1
    else:
        a['ping'] += 1
        b['ping'] += 1


def max_list(lt):
    temp = 0
    for i in lt:
        if lt.count(i) > temp:
            max_str = i
            temp = lt.count(i)
    return max_str


print(a['win1'], a['ping'], a['lose'])
print(b['win1'], b['ping'], b['lose'])
if a['win1'] == 0:
    x1 = 'B'
else:
    x1 = max_list(sorted(a['win']))
if b['win1'] == 0:
    x2 = 'B'
else:
    x2 = max_list(sorted(b['win']))

print(x1, x2)
