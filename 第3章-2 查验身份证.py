n = int(input())
flag = 1
weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
M = [1, 0, "X", 9, 8, 7, 6, 5, 4, 3, 2]
for i in range(0, n):
    t = list(input())
    integer = [int(t[i])*weight[i] if '0'<=t[i]<='9' else -100000 for i in range(0,17)]
    z = sum(integer) % 11
    if t[-1] != "X":
        if z < 0 or M[z] != int(t[-1]):
            flag = 0
            print("".join(t))
    else:
        if z != 2:
            flag = 0
            print("".join(t))
if flag == 1:
    print("All passed")
