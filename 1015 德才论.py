"""
输入第一行给出 3 个正整数，分别为：N（≤10​5​​），即考生总数；L（≥60），为录取最低分数线，
即德分和才分均不低于 L 的考生才有资格被考虑录取；H（<100），为优先录取线——德分和才分
均不低于此线的被定义为“才德全尽”，此类考生按德才总分从高到低排序；才分不到但德分到线的
一类考生属于“德胜才”，也按总分排序，但排在第一类考生之后；德才分均低于 H，但是德分不低
于才分的考生属于“才德兼亡”但尚有“德胜才”者，按总分排序，但排在第二类考生之后；其他达到
最低线 L 的考生也按总分排序，但排在第三类考生之后。
随后 N 行，每行给出一位考生的信息，包括：准考证号 德分 才分，其中准考证号为 8 位整数，德
才分为区间 [0, 100] 内的整数。数字间以空格分隔。
"""


def rank(x):
    return x[3],int(x[1]),-int(x[0])
a = [int(i) for i in input().split()]
n = a[0]
l = a[1]
h = a[2]
a = []; b = [];c = [];d = []
for i in range(n):
    x = input().split()
    if int(x[1])<l or int(x[2])<l:
        continue
    x.append(int(x[1])+int(x[2]))
    if int(x[1])>=h and int(x[2])>=h:
        a.append(x)
    elif int(x[1])>=h and int(x[2])<h:
        b.append(x)
    elif int(x[1])<h and int(x[2])<h and int(x[1])>=int(x[2]):
        c.append(x)
    else:
        d.append(x)
a = sorted(a,key=rank,reverse=True)
b = sorted(b,key=rank,reverse=True)
c = sorted(c,key=rank,reverse=True)
d = sorted(d,key=rank,reverse=True)
e = a + b + c + d
print(len(e))
for i in e:
    print(' '.join(i[:-1]))


