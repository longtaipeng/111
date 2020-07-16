dic = eval(input())
num = int(input())
dic1 = {}
count = 0
def m(a, w=count):
    w += 1
    dic1[w] = []
    for i in a:
        if type(i) is int:
            dic1[w].append(i)
        if type(i) is list:
            m(i, w)
    return dic1
dic2 = m(dic)
for key in dic2.keys():
    if key == num:
        print(len(dic2[key]))