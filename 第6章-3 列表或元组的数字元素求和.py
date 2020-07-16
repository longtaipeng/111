# 这是一个列表或元组的数字元素求和
l1 = []
def listsum(a):
    for i in a:
        if type(i) == int:
            l1.append(i)
        elif type(i) == list or type(i) == tuple:
                listsum(i)
    return l1


a = eval(input())
print(sum(listsum(a)))
