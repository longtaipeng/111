a = eval(input())
b = eval(input())
k1 = {}
for key, value in a.items():
    k1[key] = value
for key, value in b.items():
    if key not in k1.keys():
        k1[key] = value
    else:
        k1[key] += value

d3=str(dict(sorted(k1.items(),key=lambda x:x[0] if type(x[0])==int else ord(x[0]))))
d3=d3.replace(' ','')
d3=d3.replace("'",'"')
print(d3)