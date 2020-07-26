count = list(map(int, input().split(' ')))
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
n2 = []
n = []
for i in range(len(count)):
    n2.append(count[i]*number[i])

for i in ''.join(n2):
    n.append(int(i))

n1 = [i for i in n if i != 0]
m = []
s = min(n1)
m.append(str(s))
n.remove(s)
n = sorted(n)
for i in n:
    m.append(str(i))

print(''.join(m))
